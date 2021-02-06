# Libs
from time import sleep

# Color
branco = '\033[1;97m'

print(branco + "-=" * 79)
print(branco + "-- Jupy$ v1 --".center(158))
print(branco + "-=" * 79 + branco)


# Introdução
print("Óla! Me chamo Jupy.")
print("Fui criado, com o objetivo de responder ao usúario,")
print("ou seja, você. Perguntas as quais tenha a em meu BD(Banco de dados).")
print("Espero conseguir te ajudar.")

sleep(2)

print(branco + "-=" * 79 + branco)

def jupyv1():
    from time import sleep
    jupy = "Jupy$"

    # Comands Jupy
    print("-- Comandos Jupy --".center(158))

    print(branco + "-=" * 79 + branco)

    print("Jupy List - Lista de tipo de informações que ele tem registradas")
    print("Jupy Copy - Copyrigth do Jupy")

    print(branco + "-=" * 79 + branco)

    print("[ 1 ] COMANDO JUPY")
    print("[ 2 ] HARDWARE")
    print("[ 3 ] LINGUAGEM DE PROGRAMAÇÃO")
    print("[ 4 ] CONSOLE")

    nicho = int(input("Opção: "))
    while nicho != 1 and nicho != 2 and nicho != 3 and nicho != 4:
        nicho = int(input("ERRO! Opção: "))

    print(branco + "-=" * 79 + branco)

    # Pergunta do usúario
    if nicho != 1:
        print("Jupy$: Começe a pergunta com 'o que'")

    pergunta = str(input("Pergunta$: ")).lower()

    print(branco + "-=" * 79 + branco)
    
    ## Time
    sleep(2)

    # Banco de dados de respostas

    def breaklin():
        print("")

    ## NT comando secreto
    if "Key Master: NT UOU UOU" in pergunta:
        pass

    ## Comandos Jupy
    if nicho == 1:
        if pergunta == "jupy list":
            print("-- Jupy$ list --".center(158))
            print("° Hardware")
            print("° Linguagem de programação")
            print("° Consoles")
        
        elif pergunta == "jupy copy":
            print("-- (C) NT Developer --".center(158))

    ## Componentes eletrônicos
    if nicho == 2:
        if pergunta == "o que e cpu?" or pergunta == "o que e cpu" or pergunta == "o que e uma cpu?" or pergunta == "o que e uma cpu" or pergunta == "o que significa cpu?" or pergunta == "o que significa cpu":
            print("Jupy$: CPU é a sigla para Central Process Unit, ou Unidade Central de Processamento.")
            print("Ele é o principal item de hardware do computador, que também é conhecido como processador.")
            print("A CPU é responsável por calcular e realizar tarefas determinadas pelo usuário e é considerado o cérebro do PC.")

        elif pergunta == "o que e gpu?" or pergunta == "o que e gpu" or pergunta == "o que e uma gpu?" or pergunta == "o que e uma gpu" or pergunta == "o que significa gpu?" or pergunta == "o que significa gpu":
            print("Jupy$: GPU (Graphics Processing Unit, ou Unidade de Processamento Gráfico), conhecido também")
            print("como VPU ou unidade de processamento visual, é um tipo de microprocessador especializado em processar gráficos")
            print("em computadores pessoais, estações de trabalho ou videogames. GPUs modernas manipulam gráficos")
            print("computadorizados com eficiência e sua estrutura de processamento paralelo os tornam mais capazes neste")
            print("tipo de trabalho que CPUs normais. Uma GPU normalmente é utilizada em placas de vídeo")
            print("(este é chamado de Vídeo Offboard ou Placa de Vídeo Dedicada), mas versões simplificadas são integradas diretamente")
            print("na placas-mãe o que é chamado de Acelerador Gráfico Integrado ou Placa de Vídeo Onboard.")

        elif pergunta == "o que e memoria ram?" or pergunta == "o que e memoria ram" or pergunta == "o que e uma memoria ram?" or pergunta == "o que e uma memoria ram" or pergunta == "o que significa memoria ram?" or pergunta == "o que significa memoria ram":
            print("Jupy$: A Memória de acesso randômico (português brasileiro) ou Memória de acesso aleatório (português europeu)")
            print("(do inglês Random Access Memory, frequentemente abreviado para RAM) é um tipo de memória")
            print("que permite a leitura e a escrita, utilizada como memória primária em sistemas eletrônicos digitais.")

            breaklin()

            print("Jupy$: A RAM é um componente essencial não apenas nos computadores pessoais, mas em qualquer")
            print("tipo de computador, pois é onde basicamente ficam armazenados os programas básicos operacionais.")
            print("Por mais que exista espaço de armazenamento disponível, na forma de um HDD ou memória flash, é sempre necessária")
            print("uma certa quantidade de RAM.")

        elif pergunta == "o que e placa mãe?" or pergunta == "o que e placa mãe" or pergunta == "o que e uma placa mãe?" or pergunta == "o que e uma placa mãe" or pergunta == "o que significa placa mãe?" or pergunta == "o que significa placa mãe":
            print("Jupy$: A placa-mãe (do inglês motherboard, composto de mother 'mãe' e board 'placa'; também")
            print("chamada em inglês de mainboard) é a parte do computador responsável por conectar e interligar todos os")
            print("componentes, ou seja, processador com memória RAM, disco rígido, placa gráfica, entre outros. Além de permitir o")
            print("tráfego de informação, a placa também alimenta alguns periféricos com a energia elétrica que recebe da fonte de alimentação.")

        elif pergunta == "o que e fonte?" or pergunta == "o que e fonte" or pergunta == "o que e uma fonte?" or pergunta == "o que e uma fonte" or pergunta == "o que significa fonte?" or pergunta == "o que significa fonte":
            print("Jupy$: Uma fonte de alimentação é um equipamento usado para alimentar cargas elétricas.")
            print("Cada dispositivo eletroeletrônico necessita de uma fonte para prover energia para seus componentes.")
            print("Esta energia pode variar de acordo com a carga que este equipamento usa.")
            print("Estas fontes de energia podem ser de corrente contínua como um conversor AC/DC ou um")
            print("regulador de tensão, pode ser um regulador linear, fonte de energia AC, fonte de alimentação")
            print("ininterrupta ou fonte de energia de alta tensão.")

        elif pergunta == "o que e gabinete?" or pergunta == "o que e gabinete" or pergunta == "o que e uma gabinete?" or pergunta == "o que e um gabinete":
            print("Jupy$: Um gabinete de computador, também conhecido como case, caixa, chassis, carcaça ou torre, é o")
            print("compartimento que contém a maioria dos componentes de um computador (normalmente, excluindo o monitor, teclado e mouse).")
            print("Um case de computador, às vezes, é referido metonimicamente como CPU, referindo-se a um componente situado dentro da caixa.")
            print("CPU era um termo comum nos primeiros computadores domésticos, quando outros periféricos da placa-mãe")
            print("normalmente eram alojados em seus próprios cases separados.")

            breaklin()

            print("Jupy$: Cases, geralmente, são construídos em aço (muitas vezes, SECC — aço eletrogalvanizado, laminado a frio, e bobina) ou alumínio.")
            print("Plástico é, por vezes, utilizado, e outros materiais, como madeira aparecem em cases construídos em casa.")

        ## Se não tiver nenhuma informação sobre a pergunta
        else:
            pergunta_erro = pergunta.split()
            print(f"Jupy$: Desculpa, mas não tenho nenhuma informação sobre '{pergunta_erro[-1]}' em meu banco de dados.")

    ## Linguagens de Programação
    if nicho == 3:
        if pergunta == "o que e o python?" or pergunta == "o que e o python" or pergunta == "o que e linguagem python?" or pergunta == "o que e a linguagem python" or pergunta == "o que e python?" or pergunta == "o que e python":
            print("Jupy$: Python é uma linguagem de programação de alto nível, interpretada, de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte.")
            print("Foi lançada por Guido van Rossum em 1991. Atualmente possui um modelo de desenvolvimento comunitário, aberto")
            print("e gerenciado pela organização sem fins lucrativos Python Software Foundation.")
            print("Apesar de várias partes da linguagem possuírem padrões e especificações formais, a linguagem como um todo não é formalmente")
            print("especificada. O padrão de facto é a implementação CPython.")

            breaklin()

            print("Jupy$: A linguagem foi projetada com a filosofia de enfatizar a importância do esforço do programador sobre o esforço computacional.")
            print("Prioriza a legibilidade do código sobre a velocidade ou expressividade. Combina uma sintaxe concisa e clara")
            print("com os recursos poderosos de sua biblioteca padrão e por módulos e frameworks desenvolvidos por terceiros.")

            breaklin()

            print("Jupy$: Python é uma linguagem de propósito geral de alto nível, multiparadigma, suporta o paradigma orientado a objetos,")
            print("imperativo, funcional e procedural. Possui tipagem dinâmica e uma de suas principais características é permitir a fácil leitura")
            print("do código e exigir poucas linhas de código se comparado ao mesmo programa em outras linguagens.")
            print("Devido às suas características, ela é principalmente utilizada para processamento de textos, dados científicos e criação de CGIs para páginas")
            print("dinâmicas para a web. Foi considerada pelo público a 3ª linguagem 'mais amada', de acordo com uma pesquisa conduzida")
            print("pelo site Stack Overflow em 2018, e está entre as 5 linguagens mais populares, de acordo com uma pesquisa conduzida pela RedMonk.")

            breaklin()

            print("Jupy$: O nome Python teve a sua origem no grupo humorístico britânico Monty Python, criador do")
            print("programa Monty Python's Flying Circus, embora muitas pessoas façam associação com o réptil do mesmo nome (em português, píton ou pitão).")

        elif pergunta == "o que e o javascript?" or pergunta == "o que e o javascript" or pergunta == "o que e a linguagem javascript?" or pergunta == "o que e a linguagem javascript" or pergunta == "o que e javascript?" or pergunta == "o que e javascript":
            print("Jupy$: JavaScript (frequentemente abreviado como JS) é uma linguagem de programação interpretada estruturada, de script em alto nível com tipagem")
            print("dinâmica fraca e multiparadigma (protótipos, orientado a objeto, imperativo e, funcional). Juntamente com HTML e CSS, o JavaScript")
            print("é uma das três principais tecnologias da World Wide Web. JavaScript permite páginas da Web interativas e, portanto, é uma parte essencial")
            print("dos aplicativos da web. A grande maioria dos sites usa, e todos os principais navegadores têm um mecanismo JavaScript dedicado para executá-lo.")

            breaklin()

            print("Jupy$: É atualmente a principal linguagem para programação client-side em navegadores web.")
            print("É também bastante utilizada do lado do servidor através de ambientes como o node.js.")

            breaklin()

            print("Jupy$: Como uma linguagem multiparadigma, o JavaScript suporta estilos de programação orientados a eventos, funcionais e imperativos")
            print("(incluindo orientado a objetos e prototype-based), apresentando recursos como fechamentos (closures) e funções de alta ordem comumente")
            print("indisponíveis em linguagens populares como Java e C++. Possui APIs para trabalhar com texto, matrizes, datas, expressões regulares e o DOM, mas a")
            print("linguagem em si não inclui nenhuma E/S, como instalações de rede, armazenamento ou gráficos, contando com isso no ambiente host em que está embutido.")

            breaklin()

            print("Jupy$: Foi originalmente implementada como parte dos navegadores web para que scripts pudessem ser executados do lado do cliente e interagissem")
            print("com o usuário sem a necessidade deste script passar pelo servidor, controlando o navegador, realizando comunicação assíncrona e alterando o conteúdo do")
            print("documento exibido, porém os mecanismos JavaScript agora estão incorporados em muitos outros tipos de software host, incluindo")
            print("servidores em servidores e bancos de dados da Web e em programas que não são da Web, como processadores de texto e PDF, e em tempo de")
            print("execução ambientes que disponibilizam JavaScript para escrever aplicativos móveis e de desktop, incluindo widgets de área de trabalho.")

            breaklin()

            print("Jupy$: Os termos Vanilla JavaScript e Vanilla JS se referem ao JavaScript não estendido por qualquer estrutura ou biblioteca adicional.")
            print("Scripts escritos em Vanilla JS são códigos JavaScript simples.")

            print("Jupy$: Embora existam semelhanças entre JavaScript e Java, incluindo o nome da linguagem, a sintaxe e as respectivas bibliotecas padrão, as duas")
            print("linguagens são distintas e diferem muito no design; JavaScript foi influenciado por linguagens de programação como Self e Scheme.")

        elif pergunta == "o que e o java?" or pergunta == "o que e o java" or pergunta == "o que e linguagem java?" or pergunta == "o que e linguagem java" or pergunta == "o que e java?" or pergunta == "o que e java":
            print("Jupy$: Java é uma linguagem de programação orientada a objetos desenvolvida na década de 90 por uma equipe de programadores chefiada")
            print("por James Gosling, na empresa Sun Microsystems. Em 2008 o Java foi adquirido pela empresa Oracle Corporation.")
            print("Diferente das linguagens de programação modernas, que são compiladas para código nativo, a linguagem Java é compilada para")
            print("um bytecode que é interpretado por uma máquina virtual (Java Virtual Machine, mais conhecida pela sua abreviação JVM).")
            print("A linguagem de programação Java é a linguagem convencional da Plataforma Java, mas não é a sua única linguagem.")
            print("J2ME Para programas e jogos de computador, celular, calculadoras, ou até mesmo o rádio do carro.")

        elif pergunta == "o que e c?" or pergunta == "o que e c" or pergunta == "o que e linguagem c?" or pergunta == "o que e linguagem c" or pergunta == "o que e a c?" or pergunta == "o que e a c" or pergunta == "o que e linguagem a c?" or pergunta == "o que e linguagem a c":
            print("Jupy$: C é uma linguagem de programação compilada de propósito geral, estruturada, imperativa, procedural, padronizada pela")
            print("Organização Internacional para Padronização (ISO), criada em 1972 por Dennis Ritchie na empresa AT&T Bell Labs para desenvolvimento")
            print("do sistema operacional Unix (originalmente escrito em Assembly).")

            breaklin()

            print("Jupy$: C é uma das linguagens de programação mais populares e existem poucas arquiteturas para as quais não existem compiladores para C.")
            print("C tem influenciado muitas outras linguagens de programação (por exemplo, a linguagem Java), mais notavelmente C++, que originalmente começou como uma extensão para C.")

        elif pergunta == "o que e c++?" or pergunta == "o que e c++" or pergunta == "o que e linguagem c++?" or pergunta == "o que e linguagem c++" or pergunta == "o que e a c++?" or pergunta == "o que e a c++":
            print("Jupy$: C++ (em português: lê-se 'cê mais mais', em inglês lê-se see plus plus) é uma linguagem de programação compilada multi-paradigma")
            print("(seu suporte inclui linguagem imperativa, orientada a objetos e genérica) e de uso geral. Desde os anos 1990 é uma das linguagens comerciais mais")
            print("populares, sendo bastante usada também na academia por seu grande desempenho e base de utilizadores.")

            breaklin()

            print("Jupy$: Bjarne Stroustrup desenvolveu o C++ (originalmente com o nome C with Classes, que significa C com classes em português) em 1983")
            print("no Bell Labs como um adicional à linguagem C. Novas características foram adicionadas com o tempo, como funções virtuais, sobrecarga de operadores,")
            print("herança múltipla, gabaritos e tratamento de exceções. Após a padronização ISO realizada em 1998 e a posterior revisão realizada em 2003, uma nova versão da")
            print("especificação da linguagem foi lançada em dezembro de 2014, conhecida informalmente como C++17.")

        elif pergunta == "o que e c#?" or pergunta == "o que e c#" or pergunta == "o que e linguagem c#?" or pergunta == "o que e linguagem c#" or pergunta == "o que e a c#?" or pergunta == "o que e a c#":
            print("Jupy$: C# é uma linguagem de programação, multiparadigma, de tipagem forte, desenvolvida pela Microsoft como parte da plataforma .NET.")
            print("A sua sintaxe orientada a objetos foi baseada no C++ mas inclui muitas influências de outras linguagens de programação, como Object Pascal e, principalmente, Java.")
            print("O código fonte é compilado para Common Intermediate Language (CIL) que é interpretado pela máquina virtual Common Language Runtime (CLR).")
            print("C# é uma das linguagens projetadas para funcionar na Common Language Infrastructure da plataforma .NET Framework.")

        elif pergunta == "o que e lua?" or pergunta == "o que e lua" or pergunta == "o que e linguagem lua?" or pergunta == "o que e linguagem lua":
            print("Jupy$: Lua é uma linguagem de programação interpretada, de script em alto nível, com tipagem dinâmica e multiparadigma, reflexiva e leve, projetada")
            print("por Tecgraf da PUC-Rio em 1993 para expandir aplicações em geral, de forma extensível (que une partes de um programa feitas em mais de uma linguagem), para")
            print("prototipagem e para ser embarcada em softwares complexos, como jogos. Assemelha-se com Python, Ruby e Icon, entre outras.")

            breaklin()

            print("Jupy$: Lua foi criada por um time de desenvolvedores do Tecgraf da PUC-Rio, a princípio, para ser usada em um projeto da Petrobras.")
            print("Devido à sua eficiência, clareza e facilidade de aprendizado, passou a ser usada em diversos ramos da programação, como no desenvolvimento de jogos")
            print("(a Blizzard Entertainment, por exemplo, usou a linguagem no jogo World of Warcraft), controle de robôs, processamento de texto, etc.")
            print("Também é frequentemente usada como uma linguagem de propósito geral.")

            breaklin()

            print("Jupy$: Lua combina programação procedural com poderosas construções para descrição de dados, baseadas em tabelas associativas e semântica extensível.")
            print("É tipada dinamicamente, interpretada a partir de bytecodes, e tem gerenciamento automático de memória com coleta de lixo.")
            print("Essas características fazem de Lua uma linguagem ideal para configuração, automação (scripting) e prototipagem rápida.")

        elif pergunta == "o que e php?" or pergunta == "o que e php" or pergunta == "o que e linguagem php?" or pergunta == "o que e linguagem php":
            print("Jupy$: PHP (um acrônimo recursivo para 'PHP: Hypertext Preprocessor', originalmente Personal Home Page) é uma linguagem interpretada livre,")
            print("usada originalmente apenas para o desenvolvimento de aplicações presentes e atuantes no lado do servidor, capazes de gerar conteúdo dinâmico na World Wide Web.")
            print("Figura entre as primeiras linguagens passíveis de inserção em documentos HTML, dispensando em muitos casos o uso de arquivos externos para eventuais processamentos de dados.")
            print("O código é interpretado no lado do servidor pelo módulo PHP, que também gera a página web a ser visualizada no lado do cliente.")
            print("A linguagem evoluiu, passou a oferecer funcionalidades em linha de comando, e além disso, ganhou características adicionais, que possibilitaram usos adicionais do")
            print("PHP, não relacionados a web sites. É possível instalar o PHP na maioria dos sistemas operacionais, gratuitamente.")
            print("Concorrente direto da tecnologia ASP pertencente à Microsoft, o PHP é utilizado em aplicações como o MediaWiki, Facebook, Drupal, Joomla!, WordPress, Magento e o Oscommerce.")

            breaklin()

            print("Jupy$: Criado por Rasmus Lerdorf em 1995, o PHP tem a produção de sua implementação principal, referência formal da linguagem, mantida por uma organização chamada The PHP Group.")
            print("O PHP é software livre, licenciado sob a PHP License, uma licença incompatível com a GNU General Public License (GPL) devido a restrições no uso do termo PHP.")

        elif pergunta == "o que e ruby?" or pergunta == "o que e ruby" or pergunta == "o que e linguagem ruby?" or pergunta == "o que e linguagem ruby":
            print("Jupy$: Ruby é uma linguagem de programação interpretada multiparadigma, de tipagem dinâmica e forte, com gerenciamento de memória automático, originalmente planejada")
            print("e desenvolvida no Japão em 1995, por Yukihiro 'Matz' Matsumoto, para ser usada como linguagem de script. Matsumoto queria desenvolver uma linguagem de")
            print("script que fosse mais poderosa do que Perl, e mais orientada a objetos do que Python. Ruby suporta programação funcional, orientada a objetos, imperativa e reflexiva.")
            print("Foi inspirada principalmente por Python, Perl, Smalltalk, Eiffel, Ada e Lisp, sendo muito similar em vários aspectos a Python. Ruby está entre as 10 linguagens")
            print("mais populares, de acordo com uma pesquisa conduzida pela RedMonk.")

            breaklin()

            print("Jupy$: A implementação 1.8.7 padrão é escrita em C, como uma linguagem de programação de único passe. Não há qualquer especificação da linguagem, assim a implementação")
            print("original é considerada de fato uma referência. Atualmente, há várias implementações alternativas da linguagem, incluindo YARV, JRuby, Rubinius, IronRuby,")
            print("MacRuby e HotRuby, cada qual com uma abordagem diferente, com IronRuby, JRuby e MacRuby fornecendo compilação JIT e, JRuby e MacRuby também fornecendo compilação AOT.")
            print("A partir das séries 1.9 em diante Ruby passou a utilizar por padrão a YARV (Yet Another Ruby VirtualMachine) substituindo a Ruby MRI (Matz's Ruby Interpreter).")

        elif pergunta == "o que e julia?" or pergunta == "o que e julia" or pergunta == "o que e linguagem julia?" or pergunta == "o que e linguagem julia":
            print("Jupy$: Julia é uma linguagem de programação dinâmica de alto nível projetada para atender os requisitos da computação de alto desempenho numérico e científico,")
            print("sendo também eficaz para a programação de propósito geral.")

            breaklin()

            print("Jupy$: Julia é escrito em C, C++, e Scheme, usando a estrutura do compilador LLVM, enquanto a maior parte da biblioteca padrão de Julia é implementada na própria Julia.")

            breaklin()

            print("Jupy$: O desenvolvimento de Julia começou em 2009 e uma versão de código aberto foi divulgado em fevereiro de 2012. Alguns aspectos incomuns do projeto Julia")
            print("incluem ter um sistema sofisticado, com tipos paramétricos dependentes de uma linguagem de programação totalmente dinâmico e adotando expedição múltipla como seu")
            print("paradigma de programação do núcleo. Cada um desses recursos tem aparecido em dialetos Lisp, como Common Lisp e Dylan, mas a combinação dos dois em um")
            print("único idioma é único (ver recursos de linguagem). O aspecto mais notável da implementação da Julia é o seu desempenho que se compara a de linguagens compiladas de alto desempenho.")

            breaklin()

            print("Jupy$: Julia se inspira significativamente em Matlab e vários dialetos de Lisp, incluindo Scheme e Common Lisp, e compartilha muitas características com")
            print("Dylan - uma outra linguagem dinâmica múltipla orientada a expedição com a sintaxe - e Fortress, outra linguagem de programação numérica com expedição múltipla e um")
            print("sofisticado sistema de tipo paramétrico. Enquanto CLOS acrescenta expedição múltipla para Common Lisp, a adição é opt-in: funções só definidos pelo usuário explicitamente")
            print("declarados genérico pode ser estendida. Em Julia, Dylan e Fortress, por outro lado, essa extensibilidade é o padrão e funções internas do sistema são todos genéricos e extensíveis.")

        elif pergunta == "o que e go?" or pergunta == "o que e go" or pergunta == "o que e linguagem go?" or pergunta == "o que e linguagem go":
            print("Jupy$: Go é uma linguagem de programação criada pela Google e lançada em código livre em novembro de 2009. É uma linguagem compilada e focada em produtividade")
            print("e programação concorrente, baseada em trabalhos feitos no sistema operacional chamado Inferno. O projeto inicial da linguagem foi feito em setembro de 2007")
            print("por Robert Griesemer, Rob Pike e Ken Thompson. Atualmente, há implementações para Windows, Linux, Mac OS X e FreeBSD")

        elif pergunta == "o que e swift?" or pergunta == "o que e swift" or pergunta == "o que e linguagem swift?" or pergunta == "o que e linguagem swift":
            print("Jupy$: Swift é uma linguagem de programação desenvolvida pela Apple para desenvolvimento no iOS, macOS, watchOS, tvOS e Linux.")
            print("Swift foi desenvolvida para manter compatibilidade com a API Cocoa e com código existente em Objective-C.")
            print("O compilador usa a infraestrutura do LLVM e é distribuído junto do Xcode desde a versão 6.")

            breaklin()

            print("Jupy$: Foi anunciada na WWDC em 2014, conferência anual da Apple. Inicialmente um software proprietário, a partir da")
            print("versão 2.2 (dezembro de 2015) foi distribuída sob a licença Apache 2.0.")

            breaklin()

            print("Jupy$: Em março de 2017, Swift ficou entre as 10 linguagens mais populares, de acordo com o")
            print("Índice Tiobe, e atualmente está entre as 20 mais populares. De acordo com uma pesquisa conduzida pela RedMonk, está entre as 10 linguagens mais populares.")
        
        ## Se não tiver nenhuma informação sobre a pergunta
        else:
            pergunta_erro = pergunta.split()
            print(f"Jupy$: Desculpa, mas não tenho nenhuma informação sobre '{pergunta_erro[-1]}' em meu banco de dados.")

    ## Consoles
    if nicho == 4:
        if pergunta == "o que e um xbox 360?" or pergunta == "o que e um xbox 360" or pergunta == "o que e o xbox 360?" or pergunta == "o que e o xbox 360" or pergunta == "o que e xbox 360?" or pergunta == "o que e xbox 360":
            print("Jupy$: O Xbox 360 é um console de video games desenvolvido pela Microsoft. Como sucessor do Xbox original, é o segundo console da série Xbox.")
            print("Ele competiu com o PlayStation 3 da Sony e o Wii da Nintendo como parte da sétima geração de consoles.")
            print("Foi oficialmente anunciado na MTV em 12 de maio de 2005, com lançamento detalhado e informações dos jogos anunciadas mais tarde na edição de 2005 da E3.")

            breaklin()

            print("Jupy$: O Xbox 360 possui um serviço online, a Xbox Live, que foi expandida a partir de sua iteração anterior no Xbox original")
            print("e recebeu atualizações regulares durante a vida útil do console.")
            print("Disponível em variedades gratuitas e baseadas em assinatura, a Xbox Live permite aos usuários jogar jogos online; baixar jogos (através da Xbox Live Arcade)")
            print("e demos; comprar e transmitir músicas, programas de televisão e filmes através dos portais Xbox Music e Xbox Video e acessar serviços de")
            print("conteúdo de terceiros através de aplicativos de transmissão de mídia. Além dos recursos multimídia on-line, ele permite aos usuários transmitir mídia de PCs locais.")
            print("Vários periféricos foram lançados, incluindo controles sem fio, discos rígidos com armazenamento expandido e a câmera sensora de movimentos: o Kinect.")
            print("O lançamento desses serviços adicionais e periféricos ajudou a marca Xbox a crescer a partir de jogos para englobar todos os")
            print("multimídia, transformando-o em um hub para entretenimento na sala de estar.")

        elif pergunta == "o que e um xbox one?" or pergunta == "o que e um xbox one" or pergunta == "o que e o xbox one?" or pergunta == "o que e o xbox one" or pergunta == "o que e xbox one?" or pergunta == "o que e xbox one":
            print("Jupy$: Xbox One é um console de videojogos, da oitava geração, produzida pela empresa Microsoft, lançado em 2013, como a terceira edição da série Xbox")
            print("e, sucessor do Xbox 360. Competindo diretamente com os consoles PlayStation 4 e Nintendo Switch. Introduzido no mercado oito anos")
            print("após o lançamento do Xbox 360. O Xbox One apresenta jogos com gráficos de alta definição superiores aos vistos no seu antecessor.")
            print("Foi anunciado no dia 21 de maio de 2013, apresentado ao público pelo presidente de negócios de entretenimento interativo da Microsoft, Don Mattrick,")
            print("no evento especial Xbox Reveal, como o sucessor do Xbox 360. Seu lançamento oficial foi feito em novembro de 2013 custando US$ 499,00 (€ 499,00 ou R$ 2.299,00).")
            print("O codinome de desenvolvimento do Xbox One foi denominado de Durango e foi anunciado oficialmente no dia 21 de maio de 2013.")

        elif pergunta == "o que e um xbox series x?" or pergunta == "o que e um xbox series x" or pergunta == "o que e o xbox series x?" or pergunta == "o que e o xbox series x" or pergunta == "o que e xbox series x?" or pergunta == "o que e xbox series x":
            print("Jupy$: O Xbox Series X e o Series S (coletivamente chamados de Xbox Series X/S[a]) são consoles domésticos de jogos eletrônicos desenvolvidos pela Microsoft.")
            print("É a quarta geração da família de consoles Xbox; foi anunciada pela primeira vez durante a E3 2019 como Project Scarlett.")
            print("Ambos os consoles foram lançados em 10 de novembro de 2020.")

            breaklin()

            print("Jupy$: Ambos os consoles sucedem a linha atual do Xbox One, substituindo o carro-chefe do Xbox One X e os modelos de baixo custo do Xbox One S, respectivamente.")
            print("A Microsoft está priorizando o desempenho do hardware, incluindo suporte para resoluções de tela mais altas (até 8K de resolução)")
            print("e taxas de quadros, ray tracing em tempo real e uso de unidade de estado sólido de alta velocidade para reduzir o tempo de carregamento.")
            print("O Xbox Series S usa a mesma CPU e GPU, memória e armazenamento interno reduzidos e não possui uma unidade óptica.")

            breaklin()

            print("Jupy$: O Xbox Series X é alimentado por uma CPU AMD Zen 2 customizada de 7 nm com oito núcleos rodando a 3,8 GHz nominal ou quando é usado em")
            print("multithreading simultâneo (SMT), a 3,6 GHz. Um núcleo da CPU é dedicado ao sistema operacional subjacente.")
            print("A unidade de processamento gráfico também é uma unidade baseada na arquitetura gráfica RDNA 2 da AMD.")
            print("Ele tem um total de 56 unidades computacionais (CUs) com 3584 núcleos, com 52 CUs e 3328 núcleos ativados e estará rodando a uma velocidade fixa de 1.825 GHz.")
            print("Esta unidade é capaz de 12.155 teraflops de potência computacional. A unidade é fornecida com 16 GB de SDRAM GDDR6,")
            print("com 10 GB rodando a 560 GB/s para ser usado principalmente com o sistema gráfico e os outros 6 GB a 336 GB/s para as outras funções de computação.")
            print("Após contabilizar o software de sistema, aproximadamente 13,5 GB de memória estarão disponíveis para jogos e outros aplicativos, com o software de sistema apenas usando recursos do pool mais lento.")

            breaklin()

            print("Jupy$: A performance alvo do Xbox Series X é renderizar jogos em resolução 4K a 60 quadros por segundo. A Microsoft afirmou que a CPU do console será quatro vezes mais")
            print("poderosa que o Xbox One X, incluindo suporte à ray tracing em tempo real, renderização de até 120 quadros por segundo e resolução 8K através do padrão HDMI 2.1.")
            print("O console também suporta novos recursos do padrão HDMI 2.1, incluindo taxa de atualização variável (VRR) e Modo Automático de")
            print("Baixa Latência (ALLM), que estão sendo incorporados às televisões mais recentes. O console terá aceleração de hardware de áudio dedicada.")
            print("Um recurso chamado 'audio ray tracing' usará os processadores gráficos de ray tracing para processar o áudio espacial da mesma maneira para melhorar a imersão de áudio para o jogador.")

        elif pergunta == "o que e um xbox series s?" or pergunta == "o que e um xbox series s" or pergunta == "o que e o xbox series s?" or pergunta == "o que e o xbox series s" or pergunta == "o que e xbox series s?" or pergunta == "o que e xbox series s":
            print("Jupy$: O Xbox Series X e o Series S (coletivamente chamados de Xbox Series X/S[a]) são consoles domésticos de jogos eletrônicos desenvolvidos pela Microsoft.")
            print("É a quarta geração da família de consoles Xbox; foi anunciada pela primeira vez durante a E3 2019 como Project Scarlett.")
            print("Ambos os consoles foram lançados em 10 de novembro de 2020.")

            breaklin()

            print("Jupy$: Ambos os consoles sucedem a linha atual do Xbox One, substituindo o carro-chefe do Xbox One X e os modelos de baixo custo do Xbox One S, respectivamente.")
            print("A Microsoft está priorizando o desempenho do hardware, incluindo suporte para resoluções de tela mais altas (até 8K de resolução)")
            print("e taxas de quadros, ray tracing em tempo real e uso de unidade de estado sólido de alta velocidade para reduzir o tempo de carregamento.")
            print("O Xbox Series S usa a mesma CPU e GPU, memória e armazenamento interno reduzidos e não possui uma unidade óptica.")

            breaklin()

            print("Jupy$: O Xbox Series S é comparável no hardware básico ao Xbox Series X, semelhante a como o Xbox One S funciona com o")
            print("Xbox One X, mas carece de algum poder de processamento bruto. Embora execute a mesma CPU com frequências de clock um pouco mais lentas, ele usa uma")
            print("GPU mais lenta, um RNDA2 com 20 CUs a 1,55 GHz para 4 TFLOPS, em comparação com 12 TFLOPS do Series X. Ele vem com 10 GB de RAM e 512 GB de")
            print("armazenamento SSD com uma taxa de transferência de entrada/saída bruta de 2,4 GB/s e não inclui nenhuma unidade de disco óptico, exigindo que o usuário obtenha")
            print("todo o software via distribuição digital. Ele é focado para renderizar jogos nominalmente a 1440p, incluindo suporte a um upscaling de 4k) a 60 quadros por segundo, embora possa")
            print("chegar a 120 quadros por segundo nesta resolução. Apesar disso, o console tem todas as funções equivalentes ao Xbox Series X, incluindo portas, expansões e suporte a jogos.")
            print("A unidade tem um formato menor e será enviada com um case branco fosco em contraste com o case preto fosco do lançamento inicial do Series X.")

        elif pergunta == "o que e um ps2?" or pergunta == "o que e um ps2" or pergunta == "o que e o ps2?" or pergunta == "o que e o ps2" or pergunta == "o que e ps2?" or pergunta == "o que e ps2":
            print("Jupy$: O PlayStation 2 (oficialmente abreviado como PS2) é um console de jogos eletrônicos produzido pela Sony Computer Entertainment.")
            print("Foi lançado no dia 4 de março de 2000 no Japão, no dia 26 de outubro na América do Norte, e posteriormente, no dia 24 de novembro na Europa e 3 de dezembro no Brasil.")
            print("Foi o sucessor do PlayStation. O PlayStation 2 é um console de sexta geração, que competiu com o Dreamcast da Sega, o GameCube da Nintendo e o Xbox da Microsoft.")

            breaklin()

            print("Jupy$: Devido à imensa popularidade em todo o mundo, o console, assim como seus jogos, continuaram a ser fabricados mesmo após o lançamento do seu sucessor, o PlayStation 3.")
            print("Somente depois de 13 anos do seu lançamento, perto do anúncio do lançamento do PlayStation 4, que o jornal japonês Asahi Shimbun anunciou o encerramento da")
            print("fabricação do console no Japão no dia 30 de dezembro de 2012. E no dia 4 de janeiro de 2013, o jornal britânico The Guardian anunciou que a Sony")
            print("encerrou a produção dos consoles PlayStation 2 no mundo inteiro.")

            breaklin()

            print("Jupy$: O PS2 é o console de videogame mais vendido de todos os tempos. De acordo com dados provenientes da Sony de 31 de março de 2012, foram vendidas mais de") 
            print("155 milhões de unidades de PlayStation 2 e mais de 420 milhões de unidades de jogos originais do console. Foram lançados mais de 4000 jogos oficiais, licenciados para o console.")
            print("O último jogo lançado para PlayStation 2 foi Pro Evolution Soccer 2014 lançado em 8 de novembro de 2013.")

        elif pergunta == "o que e um ps3?" or pergunta == "o que e um ps3" or pergunta == "o que e o ps3?" or pergunta == "o que e o ps3" or pergunta == "o que e ps3?" or pergunta == "o que e ps3":
            print("Jupy$: O PlayStation 3 (PS3) é um console de videogames desenvolvido pela Sony Computer Entertainment. É o sucessor do PlayStation 2 e faz parte da marca PlayStation de consoles.")
            print("Foi lançado em 11 de novembro de 2006, no Japão, 17 de novembro de 2006 na América do Norte e em 23 de março de 2007 na Europa e Oceania.")
            print("O PlayStation 3 compete com o console Xbox 360 da Microsoft e o Wii da Nintendo como parte da sétima geração de consoles de videogames.")

            breaklin()

            print("Jupy$: O console foi anunciado oficialmente pela primeira vez na edição de 2005 da E3 e foi lançado no final de 2006. Foi o primeiro console a usar o disco")
            print("Blu-ray como formato de mídia para gravação de jogos, seu meio de armazenamento primário. Foi o primeiro console da Sony a ter um Sistema On-line a PSN,")
            print("a PlayStation Network, e a sua conectividade remota com o PlayStation Portable e PlayStation Vita, sendo capaz de controlar remotamente os dispositivos.")
            print("Em setembro de 2009, o modelo Slim do PlayStation 3 foi lançado. Foi removida a capacidade de hardware para executar os jogos do PlayStation 2.")
            print("Era mais leve e mais fino do que a versão original, e apresentava um logotipo redesenhado e design de marketing, bem como uma pequena mudança de start-up no software.")
            print("Um novo modelo denominado Super Slim foi lançado no final de 2012, refinando e redesenhando o console.")

            breaklin()

            print("Jupy$: O sistema teve um início com vendas ruins no mercado[10], porém conseguiu se recuperar, especialmente após a introdução do modelo Slim.")
            print("O seu sucessor, o PlayStation 4, foi lançado em 15 de novembro de 2013. Em 29 de setembro de 2015, a Sony confirmou que a produção de novos consoles iriam ser")
            print("descontinuadas na Nova Zelândia, porém o sistema permaneceu em produção em outros mercados. A fabricação de novas unidades nos Estados Unidos terminaram em outubro de 2016.")
            print("Em 2017, o Japão foi o último território em que novas unidades ainda estavam sendo produzidas até 29 de maio de 2017, quando a Sony confirmou que o PlayStation 3 era descontinuado no Japão.")

        elif pergunta == "o que e um ps4?" or pergunta == "o que e um ps4" or pergunta == "o que e o ps4?" or pergunta == "o que e o ps4" or pergunta == "o que e ps4?" or pergunta == "o que e ps4":
            print("Jupy$: A PlayStation 4 (プレイステーション4 Pureisutēshon Fō?, oficialmente abreviada como PS4) é uma consola de videojogos, da oitava geração com arquitetura x86,")
            print("produzida pela empresa Sony Interactive Entertainment e lançado em Novembro de 2013, como a quarta edição da série PlayStation, sucessora da PlayStation 3, competindo")
            print("directamente com a Wii U da Nintendo e, com a Xbox One da Microsoft.")

            breaklin()

            print("Jupy$: Foi anunciada em Fevereiro de 2013 durante uma conferência de imprensa da Sony em Nova Iorque, no evento 'PlayStation Meeting 2013' cujo tema foi 'O Futuro da PlayStation'.")
            print("Foi lançada na América do Norte a 15 de Novembro de 2013, na Europa e América do Sul a 29 de Novembro de 2013 e no Japão a 22 de Fevereiro de 2014.")
            print("A PlayStation 4 é a primeira consola da Sony a ser oficialmente e legalmente editada na China desde a PlayStation 2, depois do levantamento da proibição que durou 14 anos.")

            breaklin()

            print("Jupy$: Afastando-se da arquitectura Cell da sua antecessora, a PlayStation 4 é a primeira da série da Sony que apresenta arquitectura x86, mais especificamente com a Unidade de")
            print("Processamento Acelerado (UPA) AMD x86-64, uma plataforma amplamente usada e comum em muitos dos microcomputadores modernos. A ideia é fazer com que o desenvolvimento de jogos eletrónicos")
            print("seja mais fácil para a consola, atraindo uma ampla gama de grandes e pequenos produtores. Estas mudanças destacam o esforço da Sony para melhorar as lições aprendidas durante o")
            print("desenvolvimento, produção e lançamento da PlayStation 3. Outros recursos de hardware notáveis da PlayStation 4 incluem 8GB GDDR5 de memória, um leitor Blu-ray mais rápido e um GPU que consegue")
            print("um desempenho de 1.843 TFLOPS/s. Em conversa para a revista Edge, vários produtores de videojogos descrevem a diferença de desempenho entre a PlayStation 4 e a Xbox One como 'significativa' e 'óbvia'.")

            breaklin()

            print("Jupy$: A consola permite vários métodos de interactividade com outros serviços e aparelhos incluindo; a PlayStation App, uma aplicação que melhora e expande a interactividade com a consola usando")
            print("aparelhos iOS e Android; o Remote Play, que permite activar a PlayStation 4 à distância para continuar a jogar num segundo ecrã via PlayStation Vita ou dispositivos Xperia; o PlayStation Now, um")
            print("serviço de computação em nuvem baseado em Gaikai, que oferece videojogos e outros conteúdos em stream. Pela incorporação de um botão de partilha (SHARE) no novo comando, o DualShock 4, faz com que seja")
            print("possível exibir conteúdo que está a ser jogado e transmitido ao vivo aos amigos, ou mesmo partilhar jogos através da característica ‘Share Play’, desta maneira a Sony planeia colocar assim mais foco nos aspectos sociais da consola.")

        elif pergunta == "o que e um ps5?" or pergunta == "o que e um ps5" or pergunta == "o que e o ps5?" or pergunta == "o que e o ps5" or pergunta == "o que e ps5?" or pergunta == "o que e ps5":
            print("Jupy$: O PlayStation 5, oficialmente abreviado como PS5, é um console de jogos eletrônicos de nona geração, desenvolvido pela Sony Interactive Entertainment. Foi anunciado em outubro de 2018")
            print("e confirmado em outubro de 2019 como o quinto da série PlayStation e sucessor do PlayStation 4. O console foi lançado em 12 de novembro de 2020 na América do Norte, Austrália, Coreia do Sul, Japão, Nova Zelândia")
            print("e Singapura, e em 19 de novembro para o resto do mundo. A plataforma foi lançada em duas versões, um sistema com entrada para disco óptico compatível com Blu-ray Ultra HD para suporte a jogos lançados em mídia física ou baixados")
            print("através da PlayStation Store e uma versão digital de menor custo sem a unidade de disco, utilizando apenas o download digital.")

            breaklin()

            print("Jupy$: O PlayStation 5 possui uma unidade de estado sólido personalizada projetada para a leitura de dados de alta velocidade para permitir melhorias significativas no desempenho gráfico.")
            print("O hardware também possui uma GPU AMD personalizada capaz de fornecer suporte a Ray-tracing, displays de resolução 4K e até 120 quadros por segundo, um novo hardware de áudio para efeitos")
            print("de áudio 3D em tempo real e retrocompatibilidade com a maioria dos jogos do PlayStation 4 e PlayStation VR.")

            breaklin()

            print("Jupy$: O PlayStation 5 usa a microarquitetura Zen 2 de 7nm da AMD com uma CPU de 8 núcleos rodando em uma frequência variável limitada a 3.5 GHz. A GPU é um sistema personalizado em um chip (SoC)")
            print("baseado no RDNA 2 da AMD, com 36 unidades de computação em execução em uma frequência variável, limitada a 2.23 GHz e com capacidade de 10.28 TFLOPS. Tanto a CPU quanto a GPU são monitoradas por um sistema de impulso especial")
            print("que incorpora a tecnologia SmartShift da AMD, que ajusta a frequência desses sistemas com base nas atividades atuais de ambos os chips, para atingir o consumo de energia constante ideal e um perfil de desempenho do modelo SoC.")
            print("Por exemplo, se a CPU estiver executando em atividade mais baixa, o sistema de reforço poderá reduzir sua frequência e aumentar a frequência da GPU para permitir que ela funcione com desempenho superior sem afetar o uso de energia ou o resfriamento.")
            print("A GPU suporta a aceleração por hardware da renderização rastreada por ray tracing em tempo real.[11] Ele possui uma nova tecnologia de áudio chamada Tempest Engine, que permite não apenas que centenas de fontes de som")
            print("em um jogo sejam contabilizadas na produção de saída de áudio em comparação com 79 no PlayStation 4, mas também como esse áudio é apresentado com base no usuário final. O sistema possui 16 GB de GDDR6 SDRAM com uma largura de banda de 448 GB/s.")

            breaklin()

            print("Jupy$: Uma solução de armazenamento em um SSD personalizado foi projetado para o PlayStation 5 para aumentar as taxas de entrada/saída de dados, proporcionando tempos de carregamento rápidos.")
            print("Essa velocidade permite que os jogos sejam mais imersivos e suportem resolução 8K. O sistema base possui um SSD de 825 GB conectado por meio de uma interface de 12 canais ao sistema principal, atingindo uma taxa de transferência")
            print("de 5,5 GB/s sem compressão e entre 8 a 9 GB/s usando compressão com o protocolo Oodle Kraken da RAD Game Tools. Esse tamanho de unidade atípico foi considerado ideal para o caminho de 12 canais do sistema, em vez das")
            print("unidades mais comuns de 790 GB ou 1 TB. O armazenamento direto para jogos é expansível através de uma porta NVM Express (NVMe) M.2, enquanto o armazenamento adicional pode ser disponibilizado através de unidades compatíveis com USB.")
            print("O sistema suporta uma unidade óptica Ultra HD Blu-ray compatível com 4K. Embora a instalação do jogo a partir de um disco seja obrigatória para tirar proveito do SSD, o usuário tem algum")
            print("controle de quanto instalar, como instalar apenas os componentes multijogador de um jogo.")

        ## Se não tiver nenhuma informação sobre a pergunta
        else:
            pergunta_erro = pergunta.split()
            print(f"Jupy$: Desculpa, mas não tenho nenhuma informação sobre '{pergunta_erro[-1]}' em meu banco de dados.")


    ## Time
    sleep(2)

    print(branco + "-=" * 79 + branco)


# Loop do Jupy

user = "Azul"

while user == "Azul":
    from time import sleep
    ## Time
    sleep(2)
    
    jupyv1()

    print("-- Opções --".center(158))
    print("[ Azul ] Novamente")
    print("[ Vermelho ] Sair")

    print(branco + "-=" * 79 + branco)

    user = str(input("Opção$: ")).capitalize()
    while user != "Azul" and user != "Vermelho":
        user = str(input("ERRO! Opção$: ")).capitalize()

    print(branco + "-=" * 79 + branco)

    if user == "Azul":
        jupyv1()
    elif user == "Vermelho":
        print("Jupy$: Encerrando...".center(158))
        print(branco + "-=" * 79 + branco)
        break
