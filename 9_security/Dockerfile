FROM node:16

RUN id -u appuser 2>/dev/null || useradd -m appuser

USER appuser

WORKDIR /app

COPY package.json ./
RUN npm install
COPY . .

# Commande par défaut
CMD ["npm", "start"]