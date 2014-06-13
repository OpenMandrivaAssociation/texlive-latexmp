# revision 15878
# category Package
# catalog-ctan /graphics/metapost/contrib/macros/latexmp
# catalog-date 2007-02-23 00:16:39 +0100
# catalog-license pd
# catalog-version 1.2.1
Name:		texlive-latexmp
Version:	1.2.1
Release:	7
Summary:	Interface for LaTeX-based typesetting in MetaPost
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/latexmp
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexmp.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexmp.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The MetaPost package latexMP implements a user-friendly
interface to access LaTeX-based typesetting capabilities in
MetaPost. The text to be typeset is given as string. This
allows even dynamic text elements, for example counters, to be
used in labels. Compared to other implementations it is much
more flexible, since it can be used as direct replacement for
btex..etex, and much faster, compared for example to the
solution provided by tex.mp.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metapost/latexmp/latexmp.mp
%doc %{_texmfdistdir}/doc/metapost/latexmp/README
%doc %{_texmfdistdir}/doc/metapost/latexmp/latexmp.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2.1-2
+ Revision: 753183
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2.1-1
+ Revision: 718824
- texlive-latexmp
- texlive-latexmp
- texlive-latexmp
- texlive-latexmp

