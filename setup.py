from setuptools import setup
import json


with open('metadata.json', encoding='utf-8') as fp:
    metadata = json.load(fp)


setup(
    name='greenhill_et_al2023',
    description=metadata['title'],
    license=metadata.get('license', ''),
    url=metadata.get('url', ''),
    py_modules=['cldfbench_greenhill_et_al2023'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'cldfbench_greenhill_et_al2023=cldfbench_greenhill_et_al2023:Dataset',
        ]
    },
    install_requires=[
        'phlorest',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
