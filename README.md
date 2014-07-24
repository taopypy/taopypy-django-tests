taopypy-django-tests
====================

Estudos de testes com Django

## Porque devemos fazer testes

Os testes garatem a consistência do código em futuras modificações

- Erros de implementação de novas funcionálidades 
- Correções ou alteração em aplicação já existentes
- Garante a consistência de uma história ou tarefa
- Podem ser utilizados como documentação
- Evita reversão de código
- NÃO CORRIGEM BUGS
- NÃO EVITAM BUGS

## O que eu devo testar Django

- URLs
    Podem ser testadas para evitar erros de URL e para
    garantir que a URL ainda existe e está retornando sempre
    algum valores necessários, testando assim as Views.

- Forms
    Os forms são a abstração dos Models, cabe à eles validar informações
    antes de serem salvas. Sendo assim é importante testar suas validações

- Models
    Apenas em casos onde existe algum tipo de validação ou alteração.
    Nesse caso é possível se utilizar apenas do método full_clean
    para validar os campos.

- Managers
    Nesse caso a base deve conter dados, por fixtures e validados
    os resultados

- TemplateTags
    Toda TemplateTag precisa ser validada e não fazer requisisções
    ao banco de dados

- Validators
    Os validators são uteis para reutilizar as validaçãos de um form.

- Admin
    Algumas pessoas testam a existem do aplicativo no Admin, para garantir
    que ele está registrado no Admin.


## Como montar um cenário de testes

- fixtures: uma lista de dados pronta em JSON que deve ser carregada na base de testes antes de começar 

- setUp: cadastra valores que devem ser padrões para todos os outros testes

- tearDown: roda ao final de cada teste para manter a execução do novo teste sem informações extras que podem ser criadas durante os testes.

- client: Todo os testes possuem um Client que serve para se conectar entre as URLs do projeto ou enviar dados por POST ou GET. 

```
    Exemplos e mais informações: 
    https://docs.djangoproject.com/en/dev/topics/testing/overview/
```

## Como fazer testes em Django

    - História:
        Montar um gerenciador de animais domésticos
        - que tipo de animal
            - o animal deve estar em uma lista de animais domésticos
                - cachorro
                - gato
        - quais vacinas ele tomou
            - caso o animal tenha tomado uma vacina em menos de 3 meses
            ele não pode tomar outra vacina
        - todo animal precisa ter um número de registro único
        - todo cachorro deve ser tratado pelo Dr. Carlos
        - todo gato deve ser tratado pela Dr. João
        - todo animal tratado pelo Dr.Carlos precisa ter número de registro começado
        em 5
        - todo animal tratado pela Dr. João precisa ter número de registro começado
        em 1

## Tarefas

- Como garantir as histórias com testes
- Refatoração com a ajuda dos testes
