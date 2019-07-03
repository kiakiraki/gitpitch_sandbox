# VSCodeの
# ススメ

2019/07/03 社内LT会

---

## 前置き

普段使っているエディタは何ですか?

+++

@snap[west span-40]
![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Visual_Studio_Code_1.35_icon.svg/384px-Visual_Studio_Code_1.35_icon.svg.png)
@snapend
@snap[east span-60]
![](https://upload.wikimedia.org/wikipedia/commons/c/ca/Atom_icon.png) |
@snapend

@snap[south]
-> 便利なテクやExtensionを情報交換しましょう!
@snapend

+++

@snap[west span-50]
![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Vimlogo.svg/1280px-Vimlogo.svg.png)
@snapend
@snap[east span-50]
![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Emacs-logo.svg/956px-Emacs-logo.svg.png)
@snapend

@snap[south]
-> 心に決めた相手と添い遂げてください
@snapend

+++

@snap[midpoint span-40]
![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/883px-Jupyter_logo.svg.png)
@snapend

@snap[south]
-> モダンなエディタ/IDEの便利さを知って欲しい!
@snapend

---

## VSCodeとはなんぞや

* MicrosoftがTypeScriptを布教するために作ったエディタ
* Web系の技術を利用して開発されている
  * TypeScript/CSSで記述、Electronで動作
* "VisualStudio" という名前だが、本家とは全く別物
  * オープンソース､無料

+++

### モダンなエディタとしての一般的な機能

* 高度なコード補完
* 複数選択編集
* コマンドパレット
* GUI上でのDebug
* Gitサポート
* Extensionによる機能拡張 etc...

+++

### 今回紹介したいこと

* 機械学習エンジニア向けの便利機能
* Python開発向けの便利機能


[公式のPythonチュートリアル](https://code.visualstudio.com/docs/python/python-tutorial)が充実しているので､使い始めたい時はまずここを見ましょう

---

## 機械学習エンジニア向けの便利機能

#### Jupyter Support

#### Remote Development

+++

### Jupyter Support

* `#%%` で囲った範囲をJupyterのCellとして実行可能
* 実行結果はnotebookとしてExport可能
* 既存のnotebookのImportも可能

簡単なDemoを見せます

+++

#### Jupyterと比べて何がいいのか

* 編集機能やコード補完が圧倒的に優秀
* Gitで差分管理しやすい(普通のPythonコードなので)
* Debugしやすい

+++

### Remote Development

* エディタをリモート環境へ接続し､コード編集/実行/Debugができる
* GPUサーバで動くコードを書く時にめっちゃ便利

簡単なDemoを見せます

---

## その他の便利機能

* Python仮想環境管理
* unittestサポート
* Linterサポート
* Type Hintsサポート
