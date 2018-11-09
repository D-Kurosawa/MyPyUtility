"""ルートディレクトリ以下のファイルを全て削除するスクリプト"""
import os


def main():
    print("=" * 80)

    path = os.getcwd().replace(os.sep, '/')
    print(f"右記ディレクト支配下にあるファイルを一括削除します : {path}")

    if input_selector(':: 実行しますか？ [Y/n]  >> '):
        file_delete(path)
        print('処理完了')
    else:
        print('処理を中止しました')

    print("=" * 80)


def input_selector(msg='[Yes/No] >> '):
    """標準入力でYes or Noの入力を求めboolを返す

    :type msg: str
    :rtype: bool
    """
    dic = {'y': True, 'n': False}

    while True:
        try:
            result = dic[input(msg).lower()[0]]
            break
        except KeyError:
            pass
        print('Error! Input again.')

    return result


def file_delete(path):
    """ファイルを削除する

    :type path: str
    """
    script = os.path.abspath(__file__).replace(os.sep, '/')

    print()
    for root, _, files in os.walk(path):
        for f in files:
            file = os.path.join(root, f).replace(os.sep, '/')
            if file != script:
                print(f">> Delete : {file}")
                os.remove(os.path.join(root, file))

    print()


if __name__ == '__main__':
    main()
