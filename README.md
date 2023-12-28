# 🖼️ 💾 Upload image Django

![Preview do Projeto Blogs API](./images/Car_Shop.png)

<br />

## 📡 Sobre
#

Este é um projeto onde é possível fazer o upload de imagem utilizando o framework Django. Foi implementado dois métodos onde é possível salvar em uma pasta externa ou a url da imagem na model.
A interface não foi prioridade e sim a implementação dos métodos. Ao receber a imagem, o software redimenciona a imagem antes de salvar no banco.

<br />

## 🚀 Instalação e execução
#

<details>
<summary>Instalando e executando com Docker</summary>
<br />

Para rodar está aplicação é necessário ter **Git**, **Docker** e o **Docker Compose** instalados no seu computador. O Docker Compose precisa estar na versão **1.29** ou superior.

### 1 - Clone o repositório:

```
git clone git@github.com:vschagas/Upload_Image_Django.git
```

### 2 - Na raíz do projeto, suba o container  `backend-container` utilizando o docker-compose.

    docker-compose up -d

### 3 - Abra o navegador e cole o endereço a baixo.

    http://0.0.0.0:8000/app/


</details>
<br />

## 🛠️ Tecnologias
#

- Python
- Django
- Docker
- docker-compose
- Pillow
