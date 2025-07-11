%global packname  testthat
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.7.1
Release:          1
Summary:          Testthat code.  Tools to make testing fun :)
Group:            Sciences/Mathematics
License:          GPL
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-digest R-stringr >= 0.4 R-evaluate >= 0.4.3 R-methods 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    R-digest R-stringr >= 0.4 R-evaluate >= 0.4.3 R-methods 

%description
A testing package specifically tailored for R that's fun, flexible and
easy to set up.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# %check
# %{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/tests


%changelog
* Fri Feb 17 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.6-1
+ Revision: 775809
- Import R-testthat
- Import R-testthat

