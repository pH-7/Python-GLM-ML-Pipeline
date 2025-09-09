# 🚀 ML Python Pipeline: Logistic Regression (GLM)

**ML API** that predicts binary classes using **scikit-learn** and FastAPI.

- Model trained on breast cancer dataset
- REST API with FastAPI - real-time requests
- Docker support
- Environment variable configuration
- Citable research-ready API
- MIT Licensed

## 📂 Project Structure

```plaintext
.
├── app/                # FastAPI application
├── train/              # Training scripts
├── assets/images/      # Images, diagrams
├── requirements.txt    # Python dependencies
├── Dockerfile
├── .env.dist           # Sample environment variables
├── LICENSE.md
└── README.md
```

## 🔋 Run Locally

1. Clone the repository:
```bash
git clone https://github.com/your-username/Python_GML_MLPipeline.git
cd Python_GML_MLPipeline
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy `.env.dist` to `.env` and configure your environment variables:
```env
PORT=8000
MODEL_PATH=train/model.pkl
```

5. Train the model:
```bash
cd train/
python train_model.py
cd ..
```

6. Start the server:
```bash
uvicorn app.main:app --reload --port $PORT
```

## 🐟 Docker

1. Build the Docker image:
```bash
docker build -t ml-api .
```

2. Run the container:
```bash
docker run --env-file .env -p 8000:8000 ml-api
```

Visit `http://127.0.0.1:8000/docs` for Swagger UI.


## 👋 Author

[![Pierre-Henry Soria](https://avatars0.githubusercontent.com/u/1325411?s=200)](https://ph7.me "Pierre-Henry Soria, Software Developer")

Made with ❤️ by **[Pierre-Henry Soria](https://pierrehenry.be)**. A super passionate & enthusiastic Problem-Solver / Senior Software Engineer. Also a true cheese 🧀, ristretto ☕️, and dark chocolate lover! 😋

[![@phenrysay](https://img.shields.io/badge/x-000000?style=for-the-badge&logo=x)](https://x.com/phenrysay "Follow Me on X")  [![pH-7](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/pH-7 "My GitHub")  [![YouTube Tech Videos](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@pH7Programming/videos "My YouTube Tech Engineering Channel")  [![BlueSky](https://img.shields.io/badge/BlueSky-00A8E8?style=for-the-badge&logo=bluesky&logoColor=white)](https://bsky.app/profile/ph7.me "Follow Me on BlueSky")

## 📄 License

Distributed under the [MIT License](LICENSE.md) 🎉 Happy hacking! 🤠
