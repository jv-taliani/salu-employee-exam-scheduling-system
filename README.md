Para executar o projeto:
Clone o repositório:

git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo

Execute os testes de simulação:

python main.py

def execute(
    employee_id: UUID,
    clinic_id: UUID,
    exam_type: ExamTypeEnum,
    exam_start: datetime,
) -> tuple[bool, str]

O método execute da classe ExamSchedulerClass realiza o agendamento de um exame para um funcionário, obedecendo os seguintes fatores:

A clínica e o funcionário existem
A clínica oferece o tipo de exame solicitado
O exame está dentro do horário de funcionamento da clínica
Não há outro exame marcado no mesmo horário

Se tudo estiver correto, o exame é salvo em memória (exams.append(...)) e o método retorna:
(True, "Sheduled")
Caso algo esteja inválido, o retorno é False com a explicação.

Entradas e saídas

Agendamento com sucesso:

(True, "Sheduled")

Fora do horário:

(False, "Examination outside opening hours")

Conflito com outro exame:

(False, "Exam not scheduled due to time conflict")


Estrutura do Projeto

project/
├── clinic.py              # Classes Clinic e OpeningHours
├── employee.py            # Classe Employee
├── exam.py                # Classe Exam
├── exam_type_enum.py      # Enum de tipos de exame
├── exam_scheduler.py      # Classe ExamSchedulerClass (principal)
├── memory.py              # Listas de armazenamento + funções de busca
├── test.py                # Criação de dados simulados
main.py                    # Simulação de 3 agendamentos
README.md                  # Instruções e explicações

