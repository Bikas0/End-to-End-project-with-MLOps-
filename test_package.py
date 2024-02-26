from PracticePackage.PackageA import f1, f2
from PracticePackage.PackageA.subPackageA import f3, f4
from PracticePackage.PackageA.subPackageB import f5
import PracticePackage
import pathlib


print(pathlib.Path(PracticePackage.__file__).resolve().parent)
print(f"f1 package: {f1.print_something}")