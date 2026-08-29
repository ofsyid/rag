# Chatbot Anti Halusinasi! Bikin AI Jawab Akurat Pakai RAG, DeepSeek & TiDB
> RAG Merupakan teknik dalam kecerdasan buatan yang menggabungkan model bahasa besar (LLM) dengan pencarian data eksternal agar jawaban yang diberikan lebih akurat dan sesuai dengan fakta terkini.

## 🔒 Database Setup
Kunjungi 
```
tidb.io
``` 
> Get started
> > Personal learning or project
> > > Machine Learning Engineer
> > > > Mysql
> > > >  > Python
> > > >  > > Isi bebas nama Company/Name.

## </> Setting Database 
> Create Resource
> > Starter
> > > Instance Name: Project1
> > > > Create
> > > > > Refresh halaman

## 📝 Create Database
Run
``` text
CREATE DATABASE RAG;
```
Run
``` text
USE RAG;
```
Run
``` text
CREATE TABLE documents (
  id INT PRIMARY KEY AUTO_INCREMENT,
  text TEXT,
  embedding VECTOR(1024)
);
```
## 🖧 Connect Database
> Overview
> > Database RAG
> > > General Python (MySQL Connector)
> > > > Generate password

## ⚙️ Ollama Setup

PASTIKAN SUDAH INSTALL OLLAMA: https://ollama.com/download

Pull the model in cmd:

```bash
ollama pull deepseek-llm:latest
```

Run the model:

```bash
ollama run deepseek-llm:latest
```

## 🤖 Install Virtual Environment
Run in the cmd:

```bash
python -m venv .venv
```
## 📁 Install Library python
Untuk ubah data menjadi vektor. Run cmd:

```bash
pip install sentence-transformers
```
Untuk mengkoneksikan ke Database Tidb. Run cmd:
```bash
pip install mysql-connector-pyhton
```

## ✨ Features

* 📚 Document-based Question Answering
* 🔍 Semantic Retrieval
* 🧠 Retrieval-Augmented Generation
* 🦙 Local LLM with Ollama
* 🔒 Local AI processing

## 🛠️ Tech Stack

* 🐍 Python
* 🦙 Ollama
* 🧠 DeepSeek LLM
* 🔍 RAG
* 🔢 Embedding
* 🗄️ Vector Database


---

⭐ **If you find this project useful, consider giving it a star!**
