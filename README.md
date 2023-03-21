# Importante

Para esse projeto alguns pontos importantes ainda poderiam ser implementados. 

### Circuit Breake

    Seria interessante implementar esse padrão para poder tratar o caso em que as a APIs
    dos parceiros estão instáveis ou cairam.

### Rate Limit

    Seria importante também implementar Rate Limit para poder limitar as solicitações se necessário
    à nossa API.

### Paginação

    Seria interessante implementar a paginação com fastapi-pagination para dividir em recurso menores
    as informações solicitadas.

### Cashe (Redis) 

    Seria muito interessante também guardar os dados dessa API que criei em cashe para evitar requisições
    às APIs parceiras.

# Instruções

### Primeiro passo

Fazer o clone do projeto.

### Segundo passo:

É preciso configurar no .env as APIs dos parceiros que a nossa API vai consumir.

#### É só seguir o exemplo:

```
PARTNERS_API='["https://api1.partner1","https://api2.partner2","https://api3.partner3"]'
```

### Depois de configurar as APIs dos parceiros é só rodar o comando:

```
docker-compose up e acessar o navegador no endereço http://localhost:8888/docs
```