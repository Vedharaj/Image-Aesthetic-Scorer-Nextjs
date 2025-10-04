# 🎨 Image Aesthetic Scorer

A web application that evaluates the **aesthetic quality of images** using **Neural Image Assessment (NIMA)**. Upload an image via drag-and-drop or click-to-upload, and get an **aesthetic score** (1–10) based on the image’s visual appeal.

---

## 🚀 Features

* Drag-and-drop **image upload** with file preview.
* Single or multiple image support.
* Real-time **aesthetic scoring** using a pretrained **MobileNetV2/InceptionResNet NIMA model**.
* Modern, responsive UI built with **Next.js + Tailwind CSS**.
* Fast, lightweight backend using **FastAPI**.
* Environment variable configuration for **CORS and backend URL**.

---

## 🛠 Tech Stack

| Layer       | Technology                                               |
| ----------- | -------------------------------------------------------- |
| Frontend    | Next.js 15 (App Router), React, TypeScript, Tailwind CSS |
| Backend     | FastAPI, Python 3.11, Uvicorn                            |
| ML Model    | TensorFlow/Keras, MobileNetV2 / InceptionResNetV2 (NIMA) |
| File Upload | react-dropzone                                           |
| HTTP Client | Axios                                                    |
| Environment | dotenv, .env, NEXT_PUBLIC_BACKEND_URL                    |

---

## 📂 Project Structure

```
image-aesthetic-scorer/
├─ backend/
│  ├─ models/               # Pretrained NIMA weights
│  ├─ main.py               # FastAPI app
│  ├─ model.py              # NIMA model & prediction logic
│  └─ .env                  # Backend environment variables
├─ frontend/
│  ├─ app/                  # Next.js App Router
│  │  ├─ page.tsx           # Main UI page
│  │  └─ api/               # Optional API proxy routes
│  ├─ components/ui/        # Card/Button components
│  └─ .env.local            # Frontend environment variables
├─ README.md
├─ package.json
└─ requirements.txt
```

---

## ⚡ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<username>/image-aesthetic-scorer.git
cd image-aesthetic-scorer
```

---

### 2️⃣ Backend Setup (FastAPI)

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

**Environment variables (.env):**

```
CORS_ORIGINS=http://localhost:3000,http://localhost:3001
```

**Run the backend:**

```bash
uvicorn main:app --reload
```


---

### 3️⃣ Frontend Setup (Next.js)

```bash
cd frontend
npm install
```

**Environment variables (.env.local):**

```
NEXT_PUBLIC_BACKEND_URL=http://127.0.0.1:8000
```

**Run frontend:**

```bash
npm run dev
```

App available at: [http://localhost:3000](http://localhost:3000) (or 3001 if 3000 is in use)

---

## 🎯 Usage

1. Open the frontend in your browser.
2. Drag & drop an image or click to upload.
3. Preview the image before uploading.
4. Click **Upload & Analyze**.
5. The **aesthetic score (1–10)** will be displayed.

**Example:**

```
💎 Aesthetic Score: 8.7 / 10
```

---

## 💡 Optional Features

* **Multiple image upload**: Adjust `maxFiles` in `react-dropzone`.
* **File size limits**: Handled via Next.js `serverActionsBodySizeLimit` or FastAPI backend.
* **CORS origins**: Configurable in `.env`.

---

## 🌐 Deployment

* **Frontend**: Vercel (Next.js App Router)
* **Backend**: Render
* Set `.env` variables for production domains.
* Ensure backend allows **CORS** from frontend production URL.

---

## 🖼 Screenshots / Demo

![ Upload & Score Result](https://i.ibb.co/bRzxPtTh/2.jpg)

---

## 🤝 Contributing

1. Fork the repository
2. Create a branch: `git checkout -b feature/my-feature`
3. Commit changes: `git commit -m "Add feature"`
4. Push: `git push origin feature/my-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** – see `LICENSE` file for details.

---

## 🔗 References

* [Neural Image Assessment (NIMA) GitHub](https://github.com/titu1994/neural-image-assessment)
* [Next.js App Router Documentation](https://nextjs.org/docs/app)
* [FastAPI Documentation](https://fastapi.tiangolo.com/)
* [react-dropzone Documentation](https://react-dropzone.js.org/)
