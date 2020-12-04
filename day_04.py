#%% Init data classes
from dataclasses import dataclass, asdict
from typing import Type, TypeVar
import re

# noinspection PyTypeChecker
T = TypeVar("T", bound="Passport")


@dataclass
class Passport:
    byr: str = ""
    iyr: str = ""
    eyr: str = ""
    hgt: str = ""
    hcl: str = ""
    ecl: str = ""
    pid: str = ""
    cid: str = ""

    @classmethod
    def from_string(cls: Type[T], info: str) -> T:
        # I guess this an IDE bug as creating a dict from a generator should be valid
        # noinspection PyTypeChecker
        return Passport(
            **dict(p.split(":") for p in info.strip().replace("\n", " ").split())
        )

    def is_valid(self, excludes: list[str] = ("cid",), strict: bool = False) -> bool:
        def check_year_bounds(year: str, min_bound: int, max_bound: int) -> bool:
            return year.isdigit() and min_bound <= int(year) <= max_bound

        def check_height(height: str) -> bool:
            match = re.match(r"^(\d{2,3})(cm|in)$", height)
            if match:
                value, unit = match.groups()
                value = int(value)
                return 150 <= value <= 193 if unit == "cm" else 59 <= value <= 76
            return False

        complete = all(v != "" for k, v in asdict(self).items() if k not in excludes)
        if strict:
            return (
                complete
                and check_year_bounds(self.byr, 1920, 2002)
                and check_year_bounds(self.iyr, 2010, 2020)
                and check_year_bounds(self.eyr, 2020, 2030)
                and check_height(self.hgt)
                and bool(re.match(r"^#[0-9a-f]{6}$", self.hcl))
                and self.ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                and bool(re.match(r"^\d{9}$", self.pid))
            )

        return complete


#%% Check valid passports (Part 1)
with open("day_04_input.txt") as input_data:
    passport_infos = input_data.read().strip().split("\n\n")

print(
    f"Valid passports: {sum(Passport.from_string(s).is_valid() for s in passport_infos)}"
)

#%% Validate passport values (Part 2)
print(
    f"Valid passports: {sum(Passport.from_string(s).is_valid(strict=True) for s in passport_infos)}"
)
