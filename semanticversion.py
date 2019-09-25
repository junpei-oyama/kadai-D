class SemanticVersion:
    def __init__(self, major, minor, patch):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        return f'{self.major}.{self.minor}.{self.patch}'

    def patch_version_up(self):
        self.patch += 1
        return self

    def minor_version_up(self):
        self.minor += 1
        self.patch = 0
        return self

    def major_version_up(self):
        self.major += 1
        self.minor = 0
        self.patch = 0
        return self


def main():
    py370 = SemanticVersion(major=3, minor=7, patch=0)

    # 等価である場合
    print(SemanticVersion(3, 7, 0) == py370)  # True

    # 等価でない場合
    print(SemanticVersion(3, 7, 1) == py370)  # False

    print()

    # Python3.7.0というバージョンを表現したもの
    py370 = SemanticVersion(major=3, minor=7, patch=0)

    print('3.7.0' == str(py370))  # True

    print()

    # Python3.7.0 というバージョンを表現したもの
    py370 = SemanticVersion(major=3, minor=7, patch=0)

    py371 = py370.patch_version_up()
    print(SemanticVersion(3, 7, 1) == py371)  # True

    print()

    # Python3.7.0 というバージョンを表現したもの
    py370 = SemanticVersion(major=3, minor=7, patch=0)

    py380 = py370.minor_version_up()
    print(SemanticVersion(3, 8, 0) == py380)  # True

    print()

    # Python3.7.0 というバージョンを表現したもの
    py370 = SemanticVersion(major=3, minor=7, patch=0)

    py400 = py370.major_version_up()
    print(SemanticVersion(4, 0, 0) == py400)  # True


if __name__ == '__main__':
    main()
