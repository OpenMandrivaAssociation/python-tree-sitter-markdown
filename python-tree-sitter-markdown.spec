Name:		python-tree-sitter-markdown
Version:	0.5.1
Release:	1
Summary:	Tree-sitter markdown grammar (Python bindings)
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/tree-sitter-markdown
Source0:	https://files.pythonhosted.org/packages/9a/87/8f705d8f99337c8a691bcc8c22d89ddd323eb2b860a78ae2e894b9f7ade1/tree_sitter_markdown-0.5.1.tar.gz
# PyPI sdist omits src/tree_sitter/*.h
Source1:	tree-sitter-c-headers.tar.xz
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	clang
Requires:	python%{pyver}dist(tree-sitter)

%description
Tree-sitter grammar for markdown, compiled from source. Used by
Aider's grep-ast repo-map.

%prep
%autosetup -n tree_sitter_markdown-0.5.1
tar -C tree-sitter-markdown/src -xf %{SOURCE1}

%build

%install
export CC=clang
python -m pip install \
	--no-deps --no-build-isolation --no-compile \
	--root %{buildroot} --prefix %{_prefix} \
	.

%files
%doc README.md
%license LICENSE
%{python_sitearch}/tree_sitter_markdown*
