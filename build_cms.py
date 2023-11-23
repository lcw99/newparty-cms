import os
import glob
import json

out_file = "documents.json"
out = open(out_file, "w")

doc = []
for path in glob.glob('*.md', recursive=False):
    print(path)
    with open(path, "r") as f:
        title = f.readline()
        content = f.read()
        title = title.replace("#", "").strip()
        item = {}
        item['document'] = path
        item['title'] = title
        item['content'] = content[:500]
        doc.append(item)
            
out.write(json.dumps(doc, ensure_ascii=False, indent=2))
out.close()