# climan

***

[![PyPI Downloads](https://static.pepy.tech/badge/climan)](https://pepy.tech/projects/climan)
[![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/climan)](https://github.com/smartlegionlab/climan/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/climan?label=pypi%20downloads)](https://pypi.org/project/climan/)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/climan)](https://github.com/smartlegionlab/climan/)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/climan?style=flat-square)](https://github.com/smartlegionlab/climan/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/climan)](https://pypi.org/project/climan)
[![PyPI - Format](https://img.shields.io/pypi/format/climan)](https://pypi.org/project/climan)
[![GitHub Repo stars](https://img.shields.io/github/stars/smartlegionlab/climan?style=social)](https://github.com/smartlegionlab/climan/)
[![GitHub watchers](https://img.shields.io/github/watchers/smartlegionlab/climan?style=social)](https://github.com/smartlegionlab/climan/)
[![GitHub forks](https://img.shields.io/github/forks/smartlegionlab/climan?style=social)](https://github.com/smartlegionlab/climan/)

***

## Short Description:

___climan___ - Cross-platform config and manager for click console utilities.

***

Author and developer: ___A.A. Suvorov___

[![smartlegiondev@gmail.com](https://img.shields.io/static/v1?label=email&message=smartlegiondev@gmail.com&color=blue)](mailto:mysmartlegionlab@ya.ru)

***

## What is news:

### ___climan v0.2.1___

***

## Help:

### Install and Use:

- `pip install climan`

```python
from climan.managers import ClickManager

METADATA = {
    'name': 'Cli name',
    'title': 'Cli title',
    'description': 'Cli Description',
    'version': '0.0.0',
    'author': 'Cli Author',
    'email': 'cli@email.com',
    'url': 'https://cliurl.ru',
    'donate': 'https://clidonate.ru',
    'copyright': 'Cli copyright',
}

class CliManager(ClickManager):
    def __init__(self, metadata):
        super().__init__(metadata)

cli_man = CliManager(METADATA)
```

***

## Disclaimer of liability:

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
