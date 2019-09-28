axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
Vue.component('multiselect', window.VueMultiselect.default)

const app = new Vue({
	el: '#app',
	delimiters: ['${', '}'],
	data: {
		message: 'A Word-Hoard Unlocked',
		word: '',
		author: [],
		text:[],
		timePeriod:[],
		searchDisplay: {},
		words: [],
		texts: [],
		authors: [],
		timePeriods: [],
		currentTexts:[],
	},
	methods: {

		grabAuthor: async function(){
			const response = await axios.get('api/authors/')
			let authorList = response.data

			this.authors = authorList.map( (elem) => ({
				'first_name':elem['first_name'],
				'last_name': elem['last_name'], 
				'texts':elem['texts'],
				'pk':elem['pk'],
				'value': elem
			}))
		},

		authorLabel({first_name, last_name}){
			return `${first_name} ${last_name}`
		},

		getTexts: function() {
			this.$nextTick(()=>{

			let authorPks = this.author.map(auth => auth.pk)
			;

			this.currentTexts = this.texts.filter((text)=>authorPks.includes(text.author));

			if (this.author == 0){
			 	this.currentTexts = this.texts
			 }
			});
			
			// this.texts = this.texts.filter(text => this.author) 
			// 	this.authors.map((author) => author.pk)
			// 	.includes(text.author)

			// let filteredList = this.texts.map(function(text){
			// 	return {author: text['author'], title: text['title']}
			// }).filter((text) => text.author == this.author)

			// let x = this.texts.map((text) => ({
			// 	'author': text['author'],
			// 	'title': text['title']
			// 	}))
			// .filter((text) => text.author)
			// console.log(x)
		},

		grabText: async function(){
			const response = await axios.get('api/texts/')
			let textList = response.data

			this.texts = textList.map( (elem) => ({
				'title':elem['title'],
				'author':elem['author'],
				'pk':elem['pk'],
				'time_period': elem['time_period'],
				'value': elem
			}))

			this.grabTimePeriod();

			if (this.author == 0){
			 	this.currentTexts = this.texts
			}
		},


		textLabel({title}){
			return `${title}`
		},

		grabTimePeriod(){
			this.timePeriods = this.texts.map(period => period.time_period)
			
		},

		timePeriodLabel({period}){
			return `${period}`
		},

		searchWords: async function(){

           // POST words

       		const query = {word: this.word,
       			author: this.author,
       			text: this.text
       		}

       		const res = await axios.post('search/', query)
       		   this.searchDisplay = res.data

		},
	},
	mounted(){
		this.grabAuthor()
		this.grabText()

	},
})