name: Build APK
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Buildozer Action
        uses: ArtemSBulgakov/buildozer-action@v1
        with:
          command: android debug
      - name: Upload APK
          # Bu qism v2 dan v4 ga yangilandi
        uses: actions/upload-artifact@v4
        with:
          name: jarvis-apk
          path: bin/*.apk
