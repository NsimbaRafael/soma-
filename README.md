# Soma+ 🎓

> Soma+ é uma plataforma educacional que conecta estudantes e professores do ensino médio, facilitando o compartilhamento de resumos, exercícios e simulados. 

Com um foco em **aprendizagem colaborativa**, a plataforma oferece:
* **Fórum de dúvidas** para interação direta.
* **Gamificação** com pontuação por participação.
* **Acompanhamento de desempenho** personalizado.
* **Acessibilidade** e modernidade no ensino.

---

## 🚀 Status do Desenvolvimento
Atualmente o projeto está em fase de **configuração de ambiente e arquitetura base**.

### Log de Progresso (10/01/2026):
* [x] Configuração inicial do Django.
* [x] Configuração do ambiente virtual (`venv`).
* [x] Instalação do `whitenoise` para arquivos estáticos.
* [x] Sincronização com o repositório remoto (GitHub).
* [x] Modelagem do banco de dados para estudantes e professores.


## 🏗️ Arquitetura do Sistema

O projeto utiliza um sistema de autenticação customizado, onde o **e-mail** é o identificador principal.

### 👤 Modelo de Usuário (`Usuario`)
Implementado através da classe `AbstractUser`, permitindo perfis distintos:
- **Professor:** Acesso a ferramentas de criação de conteúdo.
- **Aluno:** Acesso a materiais e fórum.
- **Atributos:** Email (único), Telefone, Biografia, Escola, Ano Escolar e Foto de Perfil.

### 🔐 Funcionalidades de Autenticação
- **Cadastro:** Com envio de e-mail de boas-vindas e atribuição automática de permissões (`rolepermissions`).
- **Login/Logout:** Autenticação baseada em e-mail.
- **Perfil:** Visualização e edição de perfil com suporte a upload de imagens.

---

## 🛠️ Estrutura de Pastas e URLs
- `/register/`: Cadastro de novos usuários.
- `/sigin/`: Portal de acesso.
- `/profile/`: Painel do usuário (requer login).
- `/update_profile/`: Edição de informações e fotos.

## 📦 Dependências Adicionais Identificadas no Código
Além do Django, o projeto agora utiliza:
* `django-role-permissions`: Para gestão de papéis (Professor/Aluno).
* `Pillow`: Para processamento de imagens de perfil.

---

## 📝 Notas de Implementação
> **Importante:** Ao rodar o projeto pela primeira vez após estas alterações, é necessário executar:
> ```powershell
> python manage.py makemigrations
> python manage.py migrate
> ```
> Pois o `AbstractUser` altera a estrutura padrão da tabela `auth_user`.

## 🎨 Interface e Templates

O projeto utiliza o sistema de herança de templates do Django para manter a consistência visual.

### Organização de Páginas:
- **`base.html`**: Template mestre contendo o Navbar (Logotipo Soma+) e os blocos de scripts/CSS.
- **`pages/auth/`**: Contém os formulários de entrada e criação de conta.
- **`pages/profile/`**: Área logada para visualização de dados do estudante ou professor.

### Componentes de UI:
- **Mensagens (Django Messages):** Alerts de sucesso/erro integrados no topo das páginas para feedback de login e cadastro.
- **Upload de Media:** As fotos de perfil são renderizadas via `user.imagem.url`.


## 🗺️ Roadmap de Desenvolvimento

### Próxima Fase: Módulo de Conteúdo 📚
- [x] **Modelagem:** Criar modelos para `Materia`, `Resumo` e `Exercicio`.
- [x] **Upload:** Configurar o sistema para professores fazerem upload de PDFs.
- [ ] **Feed Principal:** Criar uma view que lista todos os materiais disponíveis.
- [ ] **Filtros:** Permitir filtrar materiais por ano escolar (1º, 2º, 3º ano).

### Fase Futura: Interação e Gamificação 🏆
- [ ] Sistema de comentários (Dúvidas).
- [ ] Sistema de pontos para quem compartilha materiais.

## 🧠 Lógica do App: Conteúdos
- **Objetivo:** Gerenciar o ciclo de vida dos materiais didáticos.
- **Fluxo de Trabalho:**
  1. Professor faz upload do PDF/Imagem com título e matéria.
  2. O sistema valida a permissão via `rolepermissions`.
  3. O conteúdo é indexado por `ano_escolar` para facilitar a busca do aluno.
  4. O aluno visualiza e baixa o conteúdo no feed principal.

### 📂 Estrutura Hierárquica de Conteúdo
O sistema organiza o conhecimento em três níveis de filtragem:
1. **Curso:** Segmentação por área de estudo.
2. **Ano Escolar:** Nível cronológico do estudante.
3. **Disciplina:** Matéria específica vinculada ao curso e ano.

Esta estrutura permite a entrega de conteúdos altamente segmentados e organizados.


## 📝 Lógica de Formulários (`forms.py`)

### Cadastro de Materiais
- **Campos Dinâmicos:** O formulário de upload vincula o arquivo a um `Curso` e uma `Disciplina` pré-cadastrados.
- **Segurança:** O campo `autor` é omitido no formulário para evitar que um usuário poste conteúdo em nome de outro. A atribuição é feita programaticamente na View.
- **Estilização:** Utiliza classes de CSS (Bootstrap) via `widgets` para manter a interface moderna.

## 🚀 Fluxo de Publicação de Conteúdo

1. **Validação de Sessão:** Apenas usuários autenticados (`@login_required`) acessam o upload.
2. **Tratamento de Mídia:** Utilização de `request.FILES` para processamento de PDFs e resumos.
3. **Vínculo Automático:** O sistema identifica o `request.user` e o atribui como `autor` do `Material`, garantindo a integridade dos dados.
4. **Feedback:** Sistema de mensagens confirmando o sucesso da publicação.

### ✅ Log de Correções (11/01/2026)
- [x] **Bug Fix:** Resolvido o `IntegrityError` no upload de materiais através da atribuição correta de `request.user` ao objeto antes do salvamento final.
- [x] **Ambiente:** Criado diretório `static/` na raiz, eliminando o aviso `staticfiles.W004` e preparando o projeto para estilização personalizada.

## 🚧 Próximos Passos (Desenvolvimento Atual)
- [x] Criação do template de listagem de materiais com suporte a cards.
- [x] Implementação de filtros por Disciplina no Frontend.
- [ ] Restrição de acesso à página de upload (apenas para perfis 'Professor').

### 📂 Módulo de Exibição (Feed de Estudos)
- **Otimização de Query:** Uso de `select_related` para carregar metadados de Cursos e Disciplinas com apenas uma consulta ao banco.
- **Interface:** Layout baseado em Cards para facilitar a leitura rápida por parte do estudante.
- **Acesso ao Arquivo:** Link direto para o storage de media através do atributo `.url` do modelo.