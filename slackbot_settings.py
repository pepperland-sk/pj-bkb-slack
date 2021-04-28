import os
from dotenv import load_dotenv

load_dotenv('.env')

# botアカウントのトークンを指定
API_TOKEN = os.environ.get("API_TOKEN")

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "ヒィア"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']