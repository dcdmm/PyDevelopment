1. 所需包安装
   * pip install --upgrade setuptools
   * pip install --upgrade build

2. 构建
   * ```shell
     cd pyproject.tool 文件所在目录
     
     # 其他可选参数
     # -w:仅生成轮子(wheel)
     # -s:仅生成源码
     # --outdir:output directory (defaults to {srcdir}/dist)
     python -m build
     ```

3. 安装
   * cd dist 目录
   * pip install .*whl