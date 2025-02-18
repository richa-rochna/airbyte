#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


from setuptools import find_packages, setup

MAIN_REQUIREMENTS = ["airbyte-cdk[vector-db-based]==0.53.8", "weaviate-client==3.25.2"]

TEST_REQUIREMENTS = ["pytest~=6.2", "docker", "pytest-docker"]

setup(
    name="destination_weaviate",
    description="Destination implementation for Weaviate.",
    author="Airbyte",
    author_email="contact@airbyte.io",
    packages=find_packages(),
    install_requires=MAIN_REQUIREMENTS,
    package_data={"": ["*.json"]},
    extras_require={
        "tests": TEST_REQUIREMENTS,
    },
)
