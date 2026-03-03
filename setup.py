# pylint: disable=missing-module-docstring
import re
from importlib.metadata import PackageNotFoundError, version

from setuptools import setup, find_packages

long_description = """A library for image augmentation in machine learning experiments, particularly convolutional
neural networks. Supports the augmentation of images, keypoints/landmarks, bounding boxes, heatmaps and segmentation
maps in a variety of different ways."""

INSTALL_REQUIRES = [
    "six",
    "numpy>=1.15",
    "scipy",
    "Pillow",
    "matplotlib",
    "scikit-image>=0.14.2",
    "opencv-python-headless",
    "imageio<=2.6.1; python_version<'3.5'",
    "imageio; python_version>='3.5'",
    "Shapely"
]

ALT_INSTALL_REQUIRES = {
    "opencv-python-headless": [
        "opencv-python",
        "opencv-contrib-python",
        "opencv-contrib-python-headless",
    ],
}


def is_installed(pkg_name: str) -> bool:
    try:
        version(pkg_name)
        return True
    except PackageNotFoundError:
        return False


def check_alternative_installation(main_req, alternatives):
    """If an alternative package is already installed, use that instead."""
    for alt in alternatives:
        alt_pkg_name = re.split(r"[!<>=]", alt)[0]
        if is_installed(alt_pkg_name):
            return alt
    return main_req


def get_install_requirements(main_requires, alternative_requires):
    install_requires = []
    for main_req in main_requires:
        if main_req in alternative_requires:
            main_req = check_alternative_installation(
                main_req, alternative_requires[main_req]
            )
        install_requires.append(main_req)
    return install_requires


INSTALL_REQUIRES = get_install_requirements(
    INSTALL_REQUIRES, ALT_INSTALL_REQUIRES
)

setup(
    name="imgaug",
    version="0.4.4",
    author="Alexander Jung",
    author_email="kontakt@ajung.name",
    url="https://github.com/marcown/imgaug",
    download_url="https://github.com/marcown/imgaug/archive/0.4.4.tar.gz",
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "": ["LICENSE", "README.md", "requirements.txt"],
        "imgaug": [
            "DejaVuSans.ttf",
            "quokka.jpg",
            "quokka_annotations.json",
            "quokka_depth_map_halfres.png",
        ],
        "imgaug.checks": ["README.md"],
    },
    license="MIT",
    description="Image augmentation library for deep neural networks",
    long_description=long_description,
    long_description_content_type="text/plain",
    python_requires=">=3.8",
    keywords=[
        "augmentation",
        "image",
        "deep learning",
        "neural network",
        "CNN",
        "machine learning",
        "computer vision",
        "overfitting",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
