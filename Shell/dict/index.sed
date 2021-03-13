# fix unicode problem output from pdftotext
s/é/é/g
s/ﬁ/fi/g
s/ő/ö/g
s/ö/ö/g
s/ﬀ/fi/g
s/ü/ü/g
s/ř/ř/g
s/ı́/í/g
s/Š/Š/g
s/ﬂ/fi/g
s/á/á/g
# remove possible control character
s/[]//g
# useless preposition at the beginning
s/^by //g
s/^on //g
s/^in //g
s/^for //g
s/^of //g
# for better display
s/\s*\bI*Rn\b\s*/ ℝⁿ /g
s/\s*\bI*Rd\b\s*/ ℝᵈ /g
s/\s*\bLp\b\s*/ Lₚ /g
s/\s*\bL1\b\s*/ L₁ /g
s/\s*\bL0\b\s*/ L₀ /g
# remove page numbers
s/\s+[0-9]+\s*$//g
s/[0-9]+,\s*[0-9]+\s*//g
s/,.*//g
# remove rebundant space
s/\s*-\s*/-/g
s/\s$//g
# remove invalid lines
/\b[0-9]+\b$/d
/Index/d
/^\w{0,3}$/d
