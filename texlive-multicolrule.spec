%global tl_name multicolrule
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3a
Release:	%{tl_revision}.1
Summary:	Decorative rules between columns
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/multicolrule
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multicolrule.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multicolrule.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multicolrule.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package lets you customize the appearance of the vertical rule that
appears between columns of multicolumn text. It is primarily intended to
work with the multicol package, hence its name, but also supports the
twocolumn option and \twocolumn macro provided by the standard classes
(and related classes such as the KOMA-Script equivalents). The package
depends on expl3 and xparse.

