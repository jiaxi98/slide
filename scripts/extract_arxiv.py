from arxiv2text import arxiv_to_md

pdf_url_list = [
  "https://arxiv.org/pdf/2503.16278v2",
  "https://arxiv.org/pdf/2405.19276",
  "https://arxiv.org/pdf/2312.05388",
  "https://arxiv.org/pdf/2201.03726",
]

output_dir = "arxiv"
for pdf_url in pdf_url_list:
  arxiv_to_md(pdf_url, output_dir)