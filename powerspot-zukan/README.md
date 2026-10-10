# パワスポ図鑑（試作）

日本地図の上に、パワースポットのご利益ごとの「オーラ」を色の光で表示する図鑑アプリの試作画面です。

公開中の画面：https://claude.ai/artifact/LrYaqwihW9uNs98aMPMKmH

## できること

- 地図の県をタップすると、その県に拡大してスポット一覧を表示
- スポット名・県名・ご利益で検索、ご利益別の絞り込み
- スポットの詳細、星の平均、投稿の表示。「行った！」で星とコメントを記録
- 「わたしのオーラ」：記録した場所だけを光らせ、ご利益別の内訳を表示
- ピンチ（スマホ）／ホイールとドラッグ（PC）で拡大・縮小。縮小は日本全体まで
- 広告を入れる位置のイメージとして広告枠を表示

## 制限事項・確かめていないこと

- スポットは実在する37か所のみ。星の数・投稿件数・口コミ文はすべて架空のサンプル
- 記録はその端末のブラウザにだけ保存され、他の端末や他の人には共有されない
- 新しいスポットの投稿機能は未実装
- 動作確認はPCのChromeでの画面確認と、Android実機での目視のみ。iPhoneでは未確認

## ファイル

- `index.html`：公開している画面そのもの（1ファイルで動く）
- `src/template.html`：画面のもと。`__PREFS__` の部分に地図データが入る
- `src/prefs.json`：都道府県の形（簡略化済み）
- `src/simplify.py`：地図データを作るスクリプト

地図の元データは [dataofjapan/land](https://github.com/dataofjapan/land) の `japan.geojson` を使い、`simplify.py` で軽くしています。

作り直す手順：

```
python3 simplify.py japan.geojson prefs.json
python3 -c "t=open('template.html').read();p=open('prefs.json').read();open('../index.html','w').write(t.replace('__PREFS__',p))"
```
