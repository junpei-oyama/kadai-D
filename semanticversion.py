class SemanticVersion:
    def __init__(self, major, minor, patch):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        return f'{self.major}.{self.minor}.{self.patch}'


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


if __name__ == '__main__':
    main()
