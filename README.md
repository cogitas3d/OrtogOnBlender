**OrtogOnBlender**
==================

<h2>História</h2>

No ano de 2014 iniciou-se uma parceria entre o cirurgião bucomaxilofacial, Dr. Everton da Rosa e o 3D designer * [Cicero Moraes](http://www.ciceromoraes.com.br) com o objetivo de criar uma metodologia de planejamento de cirurgia ortognática baseada em software livre. A ferramenta principal de trabalho seria o Blender 3D, poderoso software livre de modelagem e animação. No entanto, apesar de este contar com um workflow bem preparado para o campo artístico, o mesmo não poderia se dizer em relação às ciências da saúde. Dentre os muitos problemas encontrados podem ser citados: a falta de uma poderosa ferramenta de cálculos booleanos para o processo de osteotomia e criação de guias cirúrgicos, a falta de suporte e conversão de  arquivos DICOM (tomografias computadorizadas) e a distribuição difusa dos comandos pela interface, o que  dificultava em muito a utilização do software por iniciantes no mundo da computação gráfica 3D.

De 2014 a 2017 dos dois especialistas desenvolveram e lapidaram não apenas uma metodologia de uso do software livre na cirurgia ortognática, mas também uma forma de compartilhar esse conhecimento através de cursos presenciais. No segundo semestre de 2017 o OrtogOnBlender começou a ser desenvolvido e em poucos meses já contava com uma versão funcional.

<h2>Sobre o sistema</h2>

O OrtogOnBlender é um addon de planejamento digital de cirurgia ortognática, baseado no software de modelagem e animação Blender 3D e é focado na facilitação do uso de ferramentas 3D por parte de profissionais da área de cirurgia bucomaxilofacial.

Organizado em um painel na parte esquerda da 3D View, o addon tem em sua estrutura os seguintes passos:

* **Importa Tomo**: Reconstrução dos ossos e do mole em 3D, a partir de uma tomografia computadorizada.
Obs.: Este módulo se encontra em estado experimental.

* **Importar Tomo 3D/Moldes**: Importação da reconstrução da tomografia computadorizada ou digitalização de moles das arcadas dentárias, efetuadas em software externo.

* **Zoom Cena**: Elementos de visualização da cena.

* **Cria Fotogrametria**: Digitalização de faces a partir de fotografias.
Obs.: Este módulo se encontra em estado experimental.

* **Importa Fotogrametria**: Importa digitalização de face efetuada em software externo.

* **Importar Cefalometria**: Importa imagem de cefalometria para alinhamento da face.

* **Redimensiona e alinha Faces**: Redimensiona a face baseada em medida conhecida e alinha a fotogrametria em relação ao mole reconstruído a partir da tomografia.

* **Osteotomia**: Osteotomia dos ossos da cabeça, com ferramentas de booleana complexa e configura cada uma das peças separadas (coloração e nomeamento).

* **Dinâmica do Mole**: Atrela a deformação da pele em relação a movimentação dos ossos provindos da osteotomia.

* **Criação do Splint**: Configuração dos estados do planejamento digital e criação dos splints cirúrgicos, para posterior impressão 3D

<h2>Dependências</h2>

O OrtogOnBlender utiliza uma série de addons e bibliotecas/programas, alguns nativos e outros externos em relação ao Blender 3D, são eles:

<h4>Addons</h4>
* Measureit (nativo)
* 3D Navigation (nativo)
* Import Images as Planes (nativo)
* Cork on Blender - https://github.com/dfelinto/cork-on-blender	
* Cut Mesh - https://github.com/patmo141/cut_mesh
* Object Alignment - https://github.com/patmo141/object_alignment

<h4>Programas</h4>
* Meshlab (meshlabserver) - http://www.meshlab.net/
* OpenMVG - https://github.com/openMVG/openMVG
* OpenMVS - http://cdcseacave.github.io/openMVS/
* dicom2stl - https://github.com/dave3d/dicom2stl/

<h2>Como Instalar</h2>

* Baixe o arquivo em “Clone or download”
* No Blender vá em: `File` → `User Preferences` → `Addons` → `Install from file` Procure o arquivo OrtogOnBlender-master.zip, clique sobre ele e em seguida no botão: `Install from file`
* Ativar a opção `ortog:OrtogOnBlender` e configure os caminhos dos scripts expandindo a setinha do lado esquerdo.
* Para manter o addon ativo clique em: `Save User Settings`.

<h3>Agradecimentos</h3>

Pierre Moulon, Patrick Moore, Dalai Felinto, Rodrigo Dornelles, Liogi Iwaki Filho, Antônio Eduardo Izidro, Paulo Henrique  Luiz de Freitas, Vinicius de Paula Ribeiro, Richard Gravalos, José Patrício Neto, e Hugo Santos Cunha.
