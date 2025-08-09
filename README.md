# 🚀 Logistic Regression API

**ML API** that predicts binary classes using **scikit-learn** and FastAPI.

- Model trained on breast cancer dataset
- REST API with FastAPI
- Docker support

## 🔋 Run Locally

```bash
cd train/
python train_model.py

cd ..
uvicorn app.main:app --reload
```

## 🐟 Docker

```bash
docker build -t ml-api .
docker run -p 8000:8000 ml-api
```

Visit `http://127.0.0.1:8000/docs` for Swagger UI.


## 👋 Author

[![Pierre-Henry Soria](https://avatars0.githubusercontent.com/u/1325411?s=200)](https://ph7.me "Pierre-Henry Soria, Software Developer")

Made with ❤️ by **[Pierre-Henry Soria](https://pierrehenry.be)**. A super passionate & enthusiastic Problem-Solver / Senior Software Engineer. Also a true cheese 🧀, ristretto ☕️, and dark chocolate lover! 😋

[![@phenrysay](https://img.shields.io/badge/x-000000?style=for-the-badge&logo=x)](https://x.com/phenrysay "Follow Me on X") [![pH-7](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/pH-7 "My GitHub") [![YouTube Video](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtu.be/cWBuZ4DXGK4 "YouTube SucceedAI Video") [![Bluesky](https://img.shields.io/badge/bluesky-1e90ff?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjMDAwMDAwIiBoZWlnaHQ9IjI0cHgiIHZpZXdCb3g9IjAgMCAzMiAzMiIgd2lkdGg9IjI0cHgiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTMwIDZsLTIuOTk5LTEuNjY2TDMyIDMuMzQgMjMuMTg5IDAgMTYuMDA2IDUuMzQgOC44MTMgMCAwIDMuMzQgNC45OTkgNC4zMzQgMCA2bDUuMDAxIDQuODAzTDQgMjAuODFWMjRsNS4wMDEtMS42NjZMMTYgMjhMMjIuOTk5IDIyLjM0IDMyIDI0di0zLjE4OUwyNy4wMDIgMTIgMzAgNiIgLz48L3N2Zz4=)](https://bsky.app/profile/ph7s.bsky.social "Bluesky Profile")
