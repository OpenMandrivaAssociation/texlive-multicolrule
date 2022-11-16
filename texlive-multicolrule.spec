Name:		texlive-multicolrule
Version:	56366
Release:	1
Summary:	Decorative rules between columns
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/multicolrule
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multicolrule.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multicolrule.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multicolrule.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package lets you customize the appearance of the vertical
rule that appears between columns of multicolumn text. It is
primarily intended to work with the multicol package, hence its
name, but also supports the twocolumn option and \twocolumn
macro provided by the standard classes (and related classes
such as the KOMA-Script equivalents). The package depends on
expl3 and xparse.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/multicolrule
%{_texmfdistdir}/tex/latex/multicolrule
%doc %{_texmfdistdir}/doc/latex/multicolrule

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
