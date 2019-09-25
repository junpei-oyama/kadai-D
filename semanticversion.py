class SemanticVersion:
    def __init__(self, major, minor, patch):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


def main():
    py370 = SemanticVersion(major=3, minor=7, patch=0)

    # 等価である場合
    print(SemanticVersion(3, 7, 0) == py370)  # True

    # 等価でない場合
    print(SemanticVersion(3, 7, 1) == py370)  # False


if __name__ == '__main__':
    main()
