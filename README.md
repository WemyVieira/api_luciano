#### Api que predi o perfil ideal de compra para um consórcio

<details open>
 <summary><code>POST</code> <code><b>/predict</b></code> </summary>

##### Parameters

> | name      |  type     | data type               | description                                                           |
> |-----------|-----------|-------------------------|-----------------------------------------------------------------------|
> | None      |  required | object (JSON or YAML)   | N/A  |

##### body

```JSON
 
    {
        "Login": "lucianopedroso15@gmail.com",
        "Password": "Confianca",
        "Renda": 50000,
        "Genero": 1,
        "Idade": 31,
        "EstadoCivil_Casado": 1,
        "EstadoCivil_Outros": 0,
        "EstadoCivil_Solteiro":0
    }
```


##### Example cURL

```shell
curl --location 'https://apiluciano-sfgvsqlv.b4a.run/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
                "Login": "lucianopedroso15@gmail.com",
                "Password": "Confianca",
                "Renda": 50000,
                "Genero": 1,
                "Idade": 31,
                "EstadoCivil_Casado": 1,
                "EstadoCivil_Outros": 0,
                "EstadoCivil_Solteiro":0
            }'
```

</details>
