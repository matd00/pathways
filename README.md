# pathways (Python Version)


pathways is a **fast multithreaded tool** for exploring and tracing pathways within any website. This project is inspired by the original [pathways in Rust](https://github.com/YuriRDev/pathways), rewritten in Python for learning and experimentation.


## 🧰 Getting Started


### ‼️ Prerequisites
Make sure you have Python 3.8+ installed. Then install dependencies:


```bash
pip install -r requirements.txt
```


### 🏃 Run Locally
Clone the project:


```bash
git clone https://github.com/matd00/pathways.git
```


Go to the project directory:


```bash
cd pathways/src
```


Run pathways:


```bash
python main.py --url "https://yourwebsite.com"
```


## 👀 Usage


### Table of Args
| Name  | Type | Default | Description |
|---------------|----------|---------|-------------|
| `--url` | String | - | Initial URL to start scanning. |
| `--max-urls` | Integer | 1000 | Maximum number of URLs to discover. |
| `--match-str` | String | "" | Only keep URLs containing this string. |
| `--ignore` | List | [] | Ignore URLs containing any of these substrings. |
| `--concurrency` | Integer | 10 | Number of concurrent threads. |
| `--depth` | Integer | 3 | Maximum crawl depth. |


### Example


```bash
python main.py --url "https://yourwebsite.com" \
--match-str "yourwebsite.com" \
--ignore "wordpress" --ignore "wp" \
--concurrency 10 --depth 3
```


## 🧭 Roadmap
- [ ] Prevent loops (don’t re-add visited URLs).
- [ ] Improve queue handling with priority queue.
- [ ] Add `--depth` argument (done ✅).
- [ ] Add export formats (CSV, SQLite).
- [ ] Add async mode with `asyncio` and `aiohttp`.


## 📂 Project Structure
```
src/
├── interface/
│ └── database.py # Storage and saving results
├── lib.py # Core crawling logic
├── main.py # CLI + Orchestration
├── requirements.txt # Dependencies
└── README.md # Documentation
```


## 📜 License
MIT License. See `LICENSE` file for details.