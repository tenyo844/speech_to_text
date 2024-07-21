from google.cloud import translate_v2 as translate
import os

# APIキーを環境変数として設定
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '~/.config/google/third-index-428110-s0-f738e27d63f2.json'

# クライアントの作成
translate_client = translate.Client()

# 翻訳するテキスト
japanese_text = "こんにちは、日本！"

# 翻訳を実行
result = translate_client.translate(japanese_text, target_language='en')

# 翻訳結果を表示
print(result['translatedText'])
