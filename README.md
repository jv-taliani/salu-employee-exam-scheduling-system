## Como executar o projeto

```bash
# Clone o repositório
git clone https://github.com/jv-taliani/salu-employee-exam-scheduling-system.git
cd salu-employee-exam-scheduling-system
cd project

# Execute os testes de simulação
python main.py
```

## Assinatura do método

```python
def execute(
    employee_id: UUID,
    clinic_id: UUID,
    exam_type: ExamTypeEnum,
    exam_start: datetime,
) -> tuple[bool, str]
```

## Regras de agendamento

* A clínica e o funcionário existem  
* A clínica oferece o tipo de exame solicitado  
* O exame está dentro do horário de funcionamento da clínica  
* Não há outro exame marcado no mesmo horário  

Quando todas as regras são atendidas, o exame é salvo em memória (`exams.append(...)`) e o método retorna:

```python
(True, "Sheduled")
```

Se alguma regra falhar, o método retorna `False` acompanhado da explicação.

### Exemplos de entrada e saída

| Cenário                         | Retorno                                    |
|---------------------------------|--------------------------------------------|
| Agendamento com sucesso         | `(True,  "Sheduled")`                      |
| Exame fora do horário           | `(False, "Examination outside opening hours")` |
| Conflito com outro exame        | `(False, "Exam not scheduled due to time conflict")` |

## Estrutura do projeto

```
project/
├── clinic.py              # Classes Clinic e OpeningHours
├── employee.py            # Classe Employee
├── exam.py                # Classe Exam
├── exam_type_enum.py      # Enum de tipos de exame
├── exam_scheduler.py      # Classe ExamSchedulerClass (principal)
├── memory.py              # Listas de armazenamento + funções de busca
├── test.py                # Criação de dados simulados
├── main.py                # Simulação de 3 agendamentos
└── README.md              # Instruções e explicações
```
