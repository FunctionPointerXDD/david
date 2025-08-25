
## 반달곰 커피 홈페이지
[참조링크](https://127.0.0.1/menu/)
오디오 출력 소스코드
```
lang = request.args.get('lang', DEFAULT_LANG)
fp = BytesIO()
gTTS(text, "com", lang).write_to_fp(fp)
encoded_audio_data = base64.b64encode(fp.getvalue())
```
![david](/static/david.jpg)

