import nbformat

nb_path = "ML2025_Spring_HW4.ipynb"  # 改成你的文件名

nb = nbformat.read(nb_path, as_version=4)

# 删除 notebook-level widgets metadata
if "widgets" in nb.metadata:
    del nb.metadata["widgets"]

# 删除 cell-level widgets metadata（保险）
for cell in nb.cells:
    if "metadata" in cell and "widgets" in cell["metadata"]:
        del cell["metadata"]["widgets"]

nbformat.write(nb, nb_path)
print("Widget metadata removed, outputs preserved.")