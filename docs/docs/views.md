
### 5. **Documentação das Views (`views.md`)**

Aqui explicamos como as views funcionam no sistema.

```markdown
# Views

As views são responsáveis por gerenciar as requisições HTTP e renderizar as páginas do sistema. Abaixo está a documentação das principais views.

## Lista de Processos

A view `ProcessoListView` exibe uma lista de processos cadastrados.

```python
class ProcessoListView(ListView):
    model = Processo
    template_name = 'processo_list.html'
    context_object_name = 'processos'
