axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

const app = new Vue({
	el: '#app',
	delimiters: ['${', '}'],
	data: {
		message: 'A Word-Hoard Unlocked',
		word: '',
		author:'',
		text:'',
		searchDisplay: {},
		words: [],
		texts: [],
		authors: [],
	},
	methods: {

		grabAuthor: async function(){
			const response = await axios.get('api/authors/')
			let authorList = response.data

			this.authors = authorList.map( (elem) => ({
				'first_name':elem['first_name'],
				'last_name': elem['last_name'], 
				'value': elem
			}))

			
			// console.log(response.data['first_name'])
		},

		searchWords: async function(){

           // POST words 
           const res = await axios.post('search/', 
           		{word: this.word,
           		author: this.author,
           		// text: this.texts
           	})
           this.searchDisplay = res.data
           // this.word=''
        },


		// getWord: async function(){
		// 	// GET nltk response
		// 	const res = await axios.get()
		// 	this.searchDisplay = res
		// },

		grabText: async function(){
			const res = await axios.get('search/')
			this.searchDisplay = res.data
		}

	},
	mounted(){
		this.grabAuthor()

	},
})