from setuptools import setup
import json


with open('metadata.json', encoding='utf-8') as fp:
    metadata = json.load(fp)


setup(
    name='cldfbench_greenhill_et_al_subm',
    description=metadata['title'],
    license=metadata.get('license', ''),
    url=metadata.get('url', ''),
    py_modules=['cldfbench_greenhill_et_al_subm'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'cldfbench_greenhill_et_al_subm=cldfbench_greenhill_et_al_subm:Dataset',
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
