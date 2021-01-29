#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
#나는 빈집으로 가고 있습니다.     //나는 반장으로 뽑혔습니다.     //나는 이불로 침대를 덮었습니다.
#나는 학교로 달려가고 있습니다.  window에 따른 변화 window5부터 달리/VV의 유사도가 변화함
#나는 정상으로 올라갑니다.
print("Content-Type: text/html; charset=utf-8")
print()

import cgi
form = cgi.FieldStorage()
sentence = form['sentence'].value
window = form['window'].value
windowSize = window.replace("window","")


from konlpy.tag import Kkma
from konlpy.utils import pprint
kkma = Kkma()
# print('KKMA'+"\n")
# pprint(kkma.pos(sentence))
#
#
# from konlpy.tag import Komoran
# komoran = Komoran()
# print('Komoran'+"\n")
# pprint(komoran.pos(sentence))
#
#
# from konlpy.tag import Twitter
# twitter = Twitter()
# print('Twitter'+"\n")
# print(twitter.pos(sentence))
import re

pos = kkma.pos(sentence)
posSentence = ""
listToken = "<th></th>"
for word, tag in pos:
    token = word+"/"+tag
    if "로/JK" in token or "으로/JK" in token:
        token = "(으)로/JKB"
    if "/EPT" in token:
        token = token.replace("/EPT","/EP")
    if "/EFN" in token:
        token = token.replace("/EFN","/EF")
    if "/VXA" in token:
        token = token.replace("/VXA","/VX")
    if "/ECE" in token:
        token = token.replace("/ECE","/EC")
    if "/ECS" in token:
        token = token.replace("/ECS","/EC")
    if "ㅂ니다/EF" in token:
        token = token.replace("ㅂ니다/EF","ᄇ니다/EF")
    listToken = listToken + '<th>{token}</th>'.format(token=token)
    posSentence = posSentence + token + " "

listToken = listToken + '<th>Sum</th><th>Mean</th>'
#print(posSentence)
#
import pandas as pd
##Pretrained data use
##FNS
FNSdic = {}
FNSDir = "./Data/0Fold/Lo_FNS_window_" + windowSize + ".csv"

dfFNS = pd.read_csv(FNSDir)
#print(dfFNS.head())
wordsFNS = dfFNS['word'].tolist()
simsFNS = dfFNS['similarity'].tolist()
for k in range(0,len(wordsFNS)):
    FNSword = wordsFNS[k]
    if "_" in FNSword:
        FNSword = re.sub("\_\_\d\d","",FNSword)
    if FNSdic.get(FNSword) == None:
        FNSdic[FNSword] = simsFNS[k]
    else:
        pass

##DIR
DIRdic = {}
DIRDir = "./Data/0Fold/Lo_DIR_window_" + windowSize + ".csv"

dfDIR = pd.read_csv(DIRDir)
#print(dfDIR.head())
wordsDIR = dfDIR['word'].tolist()
simsDIR = dfDIR['similarity'].tolist()
for k in range(0, len(wordsDIR)):
    DIRword = wordsDIR[k]
    if "_" in DIRword:
        DIRword = re.sub("\_\_\d\d","",DIRword)
    if DIRdic.get(DIRword) == None:
        DIRdic[DIRword] = simsDIR[k]
    else:
        pass

##INS
INSdic = {}
INSDir = "./Data/0Fold/Lo_INS_window_" + windowSize + ".csv"

dfINS = pd.read_csv(INSDir)
#print(dfINS.head())
wordsINS = dfINS['word'].tolist()
simsINS = dfINS['similarity'].tolist()
for k in range(0, len(wordsINS)):
    INSword = wordsINS[k]
    if "_" in INSword:
        INSword = re.sub("\_\_\d\d","",INSword)
    if INSdic.get(INSword) == None:
        INSdic[INSword] = simsINS[k]
    else:
        pass


##판별 Similarity Based Methods
classifiedClass = ""
token = posSentence.strip().split(" ")

sentenceClassify = {}

FNSScore = 0;
DIRScore = 0;
INSScore = 0;

originClass = ""
matchNum = 0
tokenNum = 0

listFNS = "<td>FNS</td>"
listDIR = "<td>DIR</td>"
listINS = "<td>INS</td>"

nodes = [{'id': '(으)로_FNS/JKB', 'group': 1},{'id': '(으)로_INS/JKB', 'group': 2},{'id': '(으)로_DIR/JKB', 'group': 3}]
links = []

for eachToken in token:
    if FNSdic.get(eachToken.strip()) == None:
        ZeroScore = "0.000000000000000"
        listFNS = listFNS + '<td>{ZeroScore}</td>'.format(ZeroScore=ZeroScore)
        listDIR = listDIR + '<td>{ZeroScore}</td>'.format(ZeroScore=ZeroScore)
        listINS = listINS + '<td>{ZeroScore}</td>'.format(ZeroScore=ZeroScore)
        pass
    else:
        nodeinfo = {}
        nodeinfo["id"] = eachToken
        nodeinfo["group"] = 4
        nodes.append(nodeinfo)
        matchNum = matchNum + 1
        FNSscoreGet = FNSdic.get(eachToken.strip())
        DIRscoreGet = DIRdic.get(eachToken.strip())
        INSscoreGet = INSdic.get(eachToken.strip())
        FNSScore = FNSScore + FNSscoreGet
        DIRScore = DIRScore + DIRscoreGet
        INSScore = INSScore + INSscoreGet
        FNSlinkinfo = {}
        FNSlinkinfo["source"] = '(으)로_FNS/JKB'
        FNSlinkinfo["target"] = eachToken
        FNSlinkinfo["value"] = round(FNSscoreGet*20,2)
        INSlinkinfo = {}
        INSlinkinfo["source"] = '(으)로_INS/JKB'
        INSlinkinfo["target"] = eachToken
        INSlinkinfo["value"] = round(INSscoreGet*20,2)
        DIRlinkinfo = {}
        DIRlinkinfo["source"] = '(으)로_DIR/JKB'
        DIRlinkinfo["target"] = eachToken
        DIRlinkinfo["value"] = round(DIRscoreGet*20,2)
        # print(FNSlinkinfo)
        links.append(FNSlinkinfo)
        links.append(INSlinkinfo)
        links.append(DIRlinkinfo)
        listFNS = listFNS + '<td>{FNSscoreGet}</td>'.format(FNSscoreGet=FNSscoreGet)
        listDIR = listDIR + '<td>{DIRscoreGet}</td>'.format(DIRscoreGet=DIRscoreGet)
        listINS = listINS + '<td>{INSscoreGet}</td>'.format(INSscoreGet=INSscoreGet)

    tokenNum = tokenNum + 1

d3Network = {}
d3Network["nodes"] = nodes
d3Network["links"] = links

# print(d3Network)

#print(tokenNum," , ",matchNum)
FNSmean = FNSScore/matchNum
DIRmean = DIRScore/matchNum
INSmean = INSScore/matchNum

sentenceClassify["FNS"] = FNSmean
sentenceClassify["DIR"] = DIRmean
sentenceClassify["INS"] = INSmean

listFNS = listFNS + '<td>{FNSScore}</td>'.format(FNSScore=FNSScore)
listDIR = listDIR + '<td>{DIRScore}</td>'.format(DIRScore=DIRScore)
listINS = listINS + '<td>{INSScore}</td>'.format(INSScore=INSScore)

listFNS = listFNS + '<td>{FNSmean}</td>'.format(FNSmean=FNSmean)
listDIR = listDIR + '<td>{DIRmean}</td>'.format(DIRmean=DIRmean)
listINS = listINS + '<td>{INSmean}</td>'.format(INSmean=INSmean)

dic_max = max(sentenceClassify.values())
dic_min = min(sentenceClassify.values())

listFirst = ""
listSecond = ""
listThird = ""

for x1, y1 in sentenceClassify.items():
    if y1 == dic_max:
        classifiedClass = classifiedClass + x1
        if x1 in "FNS":
            listFirst = listFNS
        elif x1 in "DIR":
            listFirst = listDIR
        else:
            listFirst = listINS
    elif y1 == dic_min:
        if x1 in "FNS":
            listThird = listFNS
        elif x1 in "DIR":
            listThird = listDIR
        else:
            listThird = listINS
    else :
        if x1 in "FNS":
            listSecond = listFNS
        elif x1 in "DIR":
            listSecond = listDIR
        else:
            listSecond = listINS

if "FNS" in classifiedClass:
    classifiedClass = "Final state (FNS)"
elif "DIR" in classifiedClass:
    classifiedClass = "Directional (DIR)"
else:
    classifiedClass = "Instrumental (INS)"

print('''<!doctype html>
<html>
<head>
  <title>Function recognition</title>
  <meta charset="utf-8">
</head>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://d3js.org/d3.v4.min.js"></script>
<link href="System.css" rel="stylesheet">
<style>

.links line {{
  stroke: #999;
  stroke-opacity: 0.6;
}}

.nodes circle {{
  stroke: #fff;
  stroke-width: 1.5px;
}}

text {{
  font-family: sans-serif;
  font-size: 20px;
}}

div#vis{{
    background:#fafbfc;
}}


</style>
<body>

<header>
      <div class="collapse bg-dark" id="navbarHeader">
        <div class="container">
          <div class="row">
            <div class="col-sm-8 col-md-7 py-4">
              <h4 class="text-white">About</h4>
                <p class="text-muted">Intended construal of a polysemous word occurs within a range of words, delivering various frame-semantic meanings (Goldberg,2006) and yet purport similar interpretations (Harris,1954). In this regard, context window-a range of words surrounding a target word, affecting the determination of its characteristics-is drawing attention to the computational understanding of combinatorial properties of words.
                <br><br>
                We ask how context window addresses polysemy interpretation in Korean, a language typologically different from the major Indo-European languages investigated for this task. We report computational simulations that explore how various sizes of context window account for polysemy of -(u)lo, which manifests polysemy due to its multiple functions mapped onto one form. For this purpose, we used the Sejong corpus, with semantic annotations involving this postposition cross-verified by three native speakers of Korean (<i>κ</i>=0.95). Employing a distributional semantic model, we devised an unsupervised learning algorithm by combining Singular Value Decomposition with Positive Pointwise Mutual Information. Using cosine similarity scores between -(u)lo and its co-occurring content words, dubbed the similarity-based estimate (Dagan et al, 1993), model performance was measured through accuracy rates that the model classiﬁed test sentences by the functions of -(u)lo, with manipulation of context window size from one to ten.
                <br><br>
                Our model achieved the highest classiﬁcation accuracy rate in the window size of one, and the accuracy rates decreased as the window size increased. This trend aligns with advantages of small window sizes (Bullinaria&Levy,2007). Considering that a narrower range of context window relates more to syntactic than to sematic information (Patel et al.,1997), our model may have employed structural, rather than semantic, characteristics of tri-grams (word-target-word) for the best classiﬁcation performance. Given the networks of interlinked clusters of words and symbolic units in human cognition (<i>construct-i-con</i>; Goldberg,2006), our findings throw light on relations between a polysemous word and an abstract schema including the word, represented as context window, in addressing word-level polysemy.
                <br><br>
                <strong style="color:white">References</strong><br>
                <ul>
                <li class="text-muted">Bullinaria, John A & Joseph P. Levy. 2007. Extracting semantic representations from word co- occurrence statistics: A computational study. Behavior Research Methods 39(3). 510–526.</li>
                <li class="text-muted">Goldberg, A. E. 2006 Constructions at work: The nature of generalization in language. Oxford: Oxford University Press.</li>
                <li class="text-muted">Harris, Zellig S. 1954 Distributional Structure. WORD. 10(2-3). 146-162.</li>
                <li class="text-muted">Ido Dagan, Shaul Marcus, & Shaul Markovitch. 1993. Contextual word similarity and estimation from sparse data. In Proceedings of ACL-93, 164-171.</li>
                <li class="text-muted">Malti Patel, John A. Bullinaria, & Joseph P. Levy. 1997. Extracting semantic representations from large text corpora. In 4th Neural Computation and Psychology Workshop, London, 9–11 April 1997, 199–212.</li>
                </ul></p>
            </div>
            <div class="col-sm-4 offset-md-1 py-4">
              <h4 class="text-white">Contact</h4>
              <ul class="list-unstyled">
                <li><a href="https://seongmin-mun.github.io/MyWebsite/Seongmin/index.html" class="text-white">Seongmin Mun</a></li>
                <li><a href="https://gyuhoshin.weebly.com/" class="text-white">Gyu-ho Shin</a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div class="navbar navbar-dark bg-dark box-shadow">
        <div class="container d-flex justify-content-between">
          <a href="#" class="navbar-brand d-flex align-items-center">
            <strong>IMPRS poster: Context window size and polysemy interpretation: A case of Korean adverbial postposition <i>-(u)lo</i></strong>
          </a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarHeader" aria-controls="navbarHeader" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
        </div>
      </div>
    </header>
    <main role="main">

        <div class="container">
          <br>
          <h1 class="jumbotron-heading"><a href="index.py">Similarity Based Estimation: -(u)lo</a></h1><br>
          <form name="frm" action="process.py" method="post">
          <h4 class="jumbotron-heading"><p>Context window size</p></h4>

                <select id="op_window" name="window">
                    <option value="window1" selected="selected">window 1</option>
                    <option value="window2">window 2</option>
                    <option value="window3">window 3</option>
                    <option value="window4">window 4</option>
                    <option value="window5">window 5</option>
                    <option value="window6">window 6</option>
                    <option value="window7">window 7</option>
                    <option value="window8">window 8</option>
                    <option value="window9">window 9</option>
                    <option value="window10">window 10</option>
                </select>
                <br><br><h4 class="jumbotron-heading"><p>Input Sentence</p></h4>
                <div class="form-group shadow-textarea">
              <p><textarea class="form-control z-depth-1" id="exampleFormControlTextarea6" cols = "100" rows="10" name="sentence" placeholder="Input your sentence ..." style="background:#fafbfc">{sentence}</textarea></p>
              </div>
              <p><input type="submit" class="btn btn-primary my-2" style="float: right;" value="Analyze"></p>
          </form>
          <br><h4 class="jumbotron-heading"><p>Classified result</p></h4>
          <p class="lead text-muted"><strong>Function of -(으)로: {classifiedClass}</strong></p>
          <br><h4 class="jumbotron-heading"><p>POS taged sentence</p></h4>
          <p class="lead text-muted"><strong>{posSentence}</strong></p>
          <br><h4 class="jumbotron-heading"><p>Similarity based estimate</p></h4>
          <div id="container_table">
          <table border="1" class="table" style="margin-bottom: 0px;">
          <thead>
          {listToken}
          <tr>{listFirst}</tr>
          <tr>{listSecond}</tr>
          <tr>{listThird}</tr>
          </thead>
          </table>
          </div>
          <br><h4 class="jumbotron-heading"><p>Interlinked network</p></h4>
          <div id="vis"></div>
          <br><br>
        </div>



    </main>

  <script>
    $('#op_window option[value={window}]').prop('selected', 'selected').change();


    graph = {d3Network}



    var width = $("#vis").width(),
        height = 400;

    var svg = d3.select("#vis").append("svg")
        .attr("width", width)
        .attr("height", height);

    var color = d3.scaleOrdinal(d3.schemeCategory20);

    var simulation = d3.forceSimulation()
        .force("link", d3.forceLink().id(function(d) {{ return d.id; }}).distance(function (d) {{ return 200}}))
        .force("charge", d3.forceManyBody())
        .force("center", d3.forceCenter(width / 3, height / 2));

    var link = svg.append("g")
    .attr("class", "links")
    .selectAll("line")
    .data(graph.links)
    .enter().append("line")
    .attr("stroke-width", function(d) {{ return Math.sqrt(d.value); }});

    var node = svg.append("g")
    .attr("class", "nodes")
    .selectAll("g")
    .data(graph.nodes)
    .enter().append("g")

    var circles = node.append("circle")
    .attr("r", 20)
    .attr("fill", function(d) {{ return color(d.group); }})
    .call(d3.drag()
    .on("start", dragstarted)
    .on("drag", dragged)
    .on("end", dragended));

    var lables = node.append("text")
    .text(function(d) {{
    return d.id;
    }})
    .attr('x', 6)
    .attr('y', 3);

    node.append("title")
    .text(function(d) {{ return d.id; }});

    simulation
    .nodes(graph.nodes)
    .on("tick", ticked);

    simulation.force("link")
    .links(graph.links);

    function ticked() {{
    link
    .attr("x1", function(d) {{ return d.source.x; }})
    .attr("y1", function(d) {{ return d.source.y; }})
    .attr("x2", function(d) {{ return d.target.x; }})
    .attr("y2", function(d) {{ return d.target.y; }});

    node
    .attr("transform", function(d) {{
    return "translate(" + d.x + "," + d.y + ")";
    }})
    }}

    function dragstarted(d) {{
      if (!d3.event.active) simulation.alphaTarget(0.3).restart();
      d.fx = d.x;
      d.fy = d.y;
    }}

    function dragged(d) {{
      d.fx = d3.event.x;
      d.fy = d3.event.y;
    }}

    function dragended(d) {{
      if (!d3.event.active) simulation.alphaTarget(0);
      d.fx = null;
      d.fy = null;
    }}





  </script>



</body>
</html>
'''.format(sentence=sentence, posSentence=posSentence, classifiedClass=classifiedClass, listToken=listToken, listFirst=listFirst, listSecond=listSecond, listThird=listThird, window=window, d3Network=d3Network))
