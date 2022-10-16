from pip import List
from pkg_resources import Requirement
from setuptools import find_packages,setup
""
def get_requirements()->List[str]:
    """
    This function wil return list of requirements
    """
    requirement_list:List[str]=[]
    return requirement_list

""
setup(
name="sensor",
version="0.0.1",
author="Keerthi Karunakaram",
author_email="kvlkarunakaram@gmail.com",
packages=find_packages(),
install_requires=get_requirements(),
)