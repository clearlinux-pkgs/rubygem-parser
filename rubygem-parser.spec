#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-parser
Version  : 2.3.1.4
Release  : 8
URL      : https://rubygems.org/downloads/parser-2.3.1.4.gem
Source0  : https://rubygems.org/downloads/parser-2.3.1.4.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-parser-bin
BuildRequires : ruby
BuildRequires : rubygem-ast
BuildRequires : rubygem-coveralls
BuildRequires : rubygem-docile
BuildRequires : rubygem-gauntlet
BuildRequires : rubygem-json_pure
BuildRequires : rubygem-kramdown
BuildRequires : rubygem-minitest
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rest-client
BuildRequires : rubygem-rubygems-tasks
BuildRequires : rubygem-simplecov
BuildRequires : rubygem-simplecov-html
BuildRequires : rubygem-yard

%description
# Parser
[![Gem Version](https://badge.fury.io/rb/parser.svg)](https://badge.fury.io/rb/parser)
[![Build Status](https://travis-ci.org/whitequark/parser.svg?branch=master)](https://travis-ci.org/whitequark/parser)

%package bin
Summary: bin components for the rubygem-parser package.
Group: Binaries

%description bin
bin components for the rubygem-parser package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n parser-2.3.1.4
gem spec %{SOURCE0} -l --ruby > rubygem-parser.gemspec

%build
export LANG=C
gem build rubygem-parser.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
parser-2.3.1.4.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/parser-2.3.1.4
ruby -v -I.:lib:test test*/test_*.rb
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/parser-2.3.1.4.gem
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/.yardopts
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/CHANGELOG.md
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/CONTRIBUTING.md
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/LICENSE.txt
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/README.md
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/bin/ruby-parse
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/bin/ruby-rewrite
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/doc/AST_FORMAT.md
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/doc/CUSTOMIZATION.md
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/doc/INTERNALS.md
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/doc/css/.gitkeep
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/doc/css/common.css
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/gauntlet_parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/all.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/ast/node.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/ast/processor.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/base.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/builders/default.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/clobbering_error.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/compatibility/ruby1_8.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/compatibility/ruby1_9.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/current.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/diagnostic.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/diagnostic/engine.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/lexer.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/lexer.rl
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/lexer/dedenter.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/lexer/explanation.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/lexer/literal.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/lexer/stack_state.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/macruby.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/macruby.y
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/messages.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/meta.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/rewriter.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/ruby18.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/ruby18.y
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/ruby19.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/ruby19.y
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/ruby20.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/ruby20.y
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/ruby21.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/ruby21.y
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/ruby22.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/ruby22.y
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/ruby23.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/ruby23.y
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/ruby24.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/ruby24.y
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/rubymotion.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/rubymotion.y
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/runner.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/runner/ruby_parse.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/runner/ruby_rewrite.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/source/buffer.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/source/comment.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/source/comment/associator.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/source/map.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/source/map/collection.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/source/map/condition.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/source/map/constant.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/source/map/definition.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/source/map/for.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/source/map/heredoc.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/source/map/keyword.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/source/map/objc_kwarg.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/source/map/operator.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/source/map/rescue_body.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/source/map/send.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/source/map/ternary.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/source/map/variable.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/source/range.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/source/rewriter.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/source/rewriter/action.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/static_environment.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/syntax_error.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/lib/parser/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/parser.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/test/bug_163/fixtures/input.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/test/bug_163/fixtures/output.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/test/bug_163/rewriter.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/test/bug_163/test_runner_rewrite.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/test/helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/test/parse_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/test/racc_coverage_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/test/test_base.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/test/test_current.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/test/test_diagnostic.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/test/test_diagnostic_engine.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/test/test_encoding.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/test/test_lexer.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/test/test_lexer_stack_state.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/test/test_parse_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/test/test_parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/test/test_source_buffer.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/test/test_source_comment.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/test/test_source_comment_associator.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/test/test_source_map.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/test/test_source_range.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/test/test_source_rewriter.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/test/test_source_rewriter_action.rb
/usr/lib64/ruby/gems/2.3.0/gems/parser-2.3.1.4/test/test_static_environment.rb
/usr/lib64/ruby/gems/2.3.0/specifications/parser-2.3.1.4.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/ruby-parse
/usr/bin/ruby-rewrite
