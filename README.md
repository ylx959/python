# Python 練習

Python 學習過程的練習程式，依主題分資料夾，每個檔案以內容命名。

| 資料夾 | 內容 |
|---|---|
| `basics/` | 型別轉換、輸入、數學函式、格式化 |
| `strings/` | 字串方法、索引、輸入驗證 |
| `control_flow/` | 條件運算式、match-case、迴圈 |
| `data_structures/` | list、set、tuple、dict、推導式、排序、zip |
| `functions/` | 函式、參數、作用域、裝飾器、lambda、遞迴 |
| `modules/` | 模組、import、`__name__` |
| `oop/` | 類別、繼承、多型、組合、特殊方法、dataclass |
| `files_and_exceptions/` | 例外處理、讀寫 txt / json / csv |
| `iterators_and_generators/` | 迭代器、產生器 |
| `time_and_threading/` | 計時、日期時間、多執行緒 |
| `pyqt/` | PyQt5 視窗元件、數位時鐘 |
| `projects/` | 小專案：hangman、拉霸機、銀行程式等 |

## 環境需求

- Python 3.12 以上

## 建立虛擬環境

在專案根目錄執行：

```bash
python3 -m venv .venv
```

## 啟動虛擬環境

macOS / Linux：

```bash
source .venv/bin/activate
```

Windows：

```powershell
.venv\Scripts\activate
```

啟動後，命令列前面會出現 `(.venv)`。離開虛擬環境：

```bash
deactivate
```

## 安裝套件

```bash
pip install -r requirements.txt
```

- `PyQt5`：`pyqt/` 裡的視窗介面
- `requests`：`projects/pokemon_api.py` 的網路請求

其他程式只用到 Python 內建模組。

## 執行程式

Python 不需要先編譯，進到程式所在的資料夾直接執行：

```bash
cd data_structures
python list_methods.py
```

讀寫檔案的程式（例如 `read_txt.py`、`write_csv.py`）和 `pyqt_image.py` 使用相對路徑，要在程式所在的資料夾執行才找得到檔案。



## 注意事項

- 不要用標準函式庫的名稱替檔案命名（例如 `random.py`、`time.py`、`json.py`），否則 `import` 時會載入到自己的檔案。