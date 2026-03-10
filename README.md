# HN-Claw-Stock 📈

> AI-Powered US Stock Selection & Trading Suggestions Web Application

## 🎯 Project Goal

Building an intelligent web application for US stock selection and buy/sell trading suggestions powered by AI analysis.

## 🚧 Status

**In Development** - Proof of Concept (POC)

## 📋 Features

### Phase 1 (Core)
- [ ] Real-time US stock data fetching (Yahoo Finance)
- [ ] Stock screener with filters
- [ ] Technical indicators (MA, RSI, MACD, Bollinger Bands)
- [ ] Basic AI-powered buy/sell suggestions
- [ ] Simple web UI

### Phase 2 (Advanced)
- [ ] Portfolio tracking
- [ ] Price alerts
- [ ] Historical performance analysis
- [ ] Advanced AI insights
- [ ] User authentication

### Phase 3 (Production)
- [ ] Real-time data streaming
- [ ] Multiple data sources
- [ ] Backtesting engine
- [ ] Risk management
- [ ] Mobile responsive UI

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | React + Tailwind CSS |
| **Backend** | Python + FastAPI |
| **Data Source** | Yahoo Finance (yfinance) |
| **AI** | Qwen Models (Dashscope) |
| **Database** | SQLite (dev) / PostgreSQL (prod) |
| **Deployment** | Alibaba Cloud |

## 📁 Project Structure

```
HN-Claw-Stock/
├── frontend/           # React frontend
│   ├── src/
│   ├── public/
│   └── package.json
├── backend/            # Python backend
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── services/
│   │   └── main.py
│   ├── requirements.txt
│   └── config.py
├── data/               # Data storage
├── tests/              # Test files
├── docs/               # Documentation
└── scripts/            # Utility scripts
```

## 🚀 Quick Start

### Backend
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## 🤝 Collaboration

This project is developed with assistance from **Claw AI** 🦞

## 📄 License

TBD

## 👤 Author

**Hilbert Ng**
- GitHub: [@Hilbert-HN](https://github.com/Hilbert-HN)
- LinkedIn: [hilbert-ng](https://www.linkedin.com/in/hilbert-ng/)

---

*Last Updated: 2026-03-11*
