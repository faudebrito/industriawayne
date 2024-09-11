
### 4. **Documentação dos Modelos (`modelos.md`)**

Aqui documentamos os modelos do projeto, explicando seus campos e comportamentos.

```markdown
# Modelos

## Processo

O modelo `Processo` representa um processo dentro do sistema. Ele contém os seguintes campos:

```python
class Processo(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
