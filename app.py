from flask import Flask, render_template

app = Flask(__name__)

profile = {
    "name": "Fabio Dias Luiz",
    "title": "Analista Funcional | Analista DevOps | Análise de Processos & Testes",
    "phone": "(11) 99237-1187",
    "email": "fabiodl77@gmail.com",
    "linkedin": "https://www.linkedin.com/in/fabio-diasluiz",
    "location": "Boituva, SP – Brasil",
    "targets": [
        "Analista DevOps",
        "Analista Funcional",
        "Análise de Processos",
        "Testes e Validação",
    ],
    "summary": (
        "Profissional de TI com carreira sólida nas áreas de Suporte Técnico e Análise Funcional, "
        "com experiências em implantação e manutenção de sistemas e na implementação de melhorias de "
        "projetos em empresas de grande e médio porte. "
        "Destaque na aplicação do framework Ágil (Scrum): controle de demandas, definição de cronograma, "
        "análise de viabilidade, negociação de prazos e escopo — sempre assegurando prazo, custo e qualidade. "
        "Atuação como Analista Funcional no cliente Strategic Touch (JBS-Brasil), com forte participação em "
        "práticas de Customer Success e Customer Experience, entregando excelência em resultados e satisfação ao cliente."
    ),
    "skills": [
        {"name": "Análise Funcional",             "icon": "📊"},
        {"name": "Levantamento de Requisitos",     "icon": "📋"},
        {"name": "Documentação de Processos",      "icon": "📄"},
        {"name": "Metodologia Ágil (Scrum)",       "icon": "🔄"},
        {"name": "Testes & Validação",             "icon": "✅"},
        {"name": "Customer Success",               "icon": "🤝"},
        {"name": "Suporte a ERP",                  "icon": "🖥️"},
        {"name": "AWS Cloud",                      "icon": "devicon-amazonwebservices-plain-wordmark"},
        {"name": "Oracle Cloud Infrastructure",    "icon": "devicon-oracle-original"},
        {"name": "DevSecOps",                      "icon": "🔒"},
        {"name": "Python",                         "icon": "devicon-python-plain"},
        {"name": "SQL Server",                     "icon": "devicon-microsoftsqlserver-plain"},
        {"name": "Windows Server",                 "icon": "devicon-windows8-original"},
        {"name": "Redes & Infraestrutura",         "icon": "🌐"},
        {"name": "N8N (Automação)",                "icon": "⚙️"},
        {"name": "Inteligência Artificial",        "icon": "🤖"},
    ],
    "experiences": [
        {
            "period": "2013 – 2026",
            "role": "Analista Funcional II",
            "company": "Mercado Eletrônico S/A",
            "short": "ME",
            "size": "Empresa nacional de médio porte",
            "description": (
                "Documentação das necessidades de negócio dos clientes para desenvolvimento de sistemas, "
                "identificação de falhas e oportunidades de melhoria de processos, levantamento de requisitos "
                "e especificação funcional."
            ),
            "highlights": [
                "Avaliação de desempenho B+ no Q1-2024",
                "Prêmio de reconhecimento TOP ME no Q2-2024",
                "Atuação no cliente Strategic Touch (JBS-Brasil)",
            ],
        },
        {
            "period": "2012 – 2013",
            "role": "Analista de Suporte Sênior",
            "company": "AdSolutions Consultings",
            "short": "AS",
            "size": "Empresa nacional de pequeno porte",
            "description": "Suporte ao sistema ERP financeiro voltado à área de Publicidade e Propaganda.",
            "highlights": [],
        },
        {
            "period": "2008 – 2011",
            "role": "Analista de Suporte",
            "company": "CMNet Soluções em Informática",
            "short": "CM",
            "size": "Empresa nacional de pequeno porte",
            "description": (
                "Suporte a sistemas ERP administrativos: Contas a Pagar, Contas a Receber, Contabilidade, "
                "Condomínio, Faturamento — análise, implantação, suporte e acompanhamento."
            ),
            "highlights": [],
        },
        {
            "period": "2006 – 2007",
            "role": "Estagiário",
            "company": "Instituto Dante Pazzanese",
            "short": "IDP",
            "size": "Empresa nacional de médio porte",
            "description": "Inserção de dados no sistema referentes a cadastros e exames cardiológicos de pacientes.",
            "highlights": [],
        },
        {
            "period": "2005",
            "role": "Estagiário – Help Desk",
            "company": "Itautec",
            "short": "IT",
            "size": "Empresa nacional de grande porte",
            "description": "Suporte help desk no sistema SIAC para o cliente Grupo Pão de Açúcar.",
            "highlights": [],
        },
        {
            "period": "2002 – 2005",
            "role": "Auxiliar Administrativo",
            "company": "Y&R Propaganda",
            "short": "Y&R",
            "size": "Empresa nacional de grande porte",
            "description": "Financeiro com Contas a Pagar e Contas a Receber, almoxarifado e administrativo.",
            "highlights": [],
        },
        {
            "period": "1993 – 1998",
            "role": "Office Boy / Encarregado de Expedição",
            "company": "S&A Comunicação e Marketing Ltda",
            "short": "S&A",
            "size": "Empresa nacional de médio porte",
            "description": "Experiência inicial como Office Boy, com evolução para Encarregado de Expedição.",
            "highlights": [],
        },
    ],
    "education": [
        {
            "degree": "Graduação em Ciências da Computação",
            "institution": "Universidade Paulista – UNIP",
            "year": "Concluído em 2007",
        }
    ],
    "courses": [
        {"name": "Santander Bootcamp 2025 – Automação com N8N", "institution": "DIO",                    "year": "2025", "status": "Em andamento"},
        {"name": "IA Impressionador",                            "institution": "Hashtag Treinamentos",  "year": "2025", "status": "Em andamento"},
        {"name": "Python Impressionador",                        "institution": "Hashtag Treinamentos",  "year": "2024", "status": "Em andamento"},
        {"name": "Open English",                                 "institution": "",                       "year": "2024", "status": "Em andamento"},
        {"name": "Inteligência Artificial",                      "institution": "Conquer",                "year": "2024", "status": "Concluído"},
        {"name": "Programa de Especialização AWS (2.0)",         "institution": "CloudTreinamentos",      "year": "2024", "status": "Concluído"},
        {"name": "Oracle Cloud Infrastructure",                  "institution": "Alura",                  "year": "2023", "status": "Concluído"},
        {"name": "Treinamento DevSecOps",                        "institution": "School of Net",          "year": "2023", "status": "Concluído"},
        {"name": "AWS Fundamentos",                              "institution": "BigData Systems",        "year": "2017", "status": "Concluído"},
        {"name": "Programa de Especialização AWS",               "institution": "CloudTreinamentos",      "year": "2016", "status": "Concluído"},
        {"name": "Conceitos e Infraestrutura de Redes",          "institution": "Impacta",                "year": "2016", "status": "Concluído"},
        {"name": "Windows Server 2012 MCSA",                     "institution": "Impacta",                "year": "2015", "status": "Concluído"},
        {"name": "Introdução à Lógica de Programação",           "institution": "Impacta",                "year": "2015", "status": "Concluído"},
        {"name": "SQL Server 2014",                              "institution": "Impacta",                "year": "2015", "status": "Concluído"},
    ],
}


@app.route("/")
def index():
    return render_template("index.html", p=profile)


if __name__ == "__main__":
    app.run(debug=True)
