from setuptools import setup, find_packages


# version 파일에서 버전 가져옴

def get_version(path='version'):
    version = ""
    with open(path, 'r') as f:
        version = f.read().strip()

    return version


# requirements 파일에서 requirements 정보 가져옴
def get_requirements(path='requirements.txt'):
    reqs = []

    try:
        with open(path, 'r') as f:
            reqs = f.read().split()

        return reqs
    except Exception:
        return []


option = 'kaggle-source-only'

if option == 'kaggle-module':
    setup(
        name=option,
        version=get_version(path='version'),
        description='kaggle',
        author='dhk',
        author_email='ehdgns322@gmail.com',
        urllib='',
        install_requires=get_requirements(path='requirements.txt'),
        packages=find_packages(exclude=['venv']),
        keywords=['kaggle', 'machine-learning', 'deep-learning'],
        python_requires='>=3.6'
    )
elif option == 'kaggle-source-only':
    setup(
        name=option,
        version=get_version(path='version'),
        description='kaggle',
        author='dhk',
        author_email='ehdgns322@gmail.com',
        urllib='',
        # install_requires=get_requirements(path='requirements.txt'),
        packages=find_packages(exclude=['venv']),
        keywords=['kaggle', 'machine-learning', 'deep-learning'],
        python_requires='>=3.6'
    )
